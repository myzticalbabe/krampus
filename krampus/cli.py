# coding: utf-8
"""krampus.py -- PROJECT KRAMPUS front door.

KRAMPUS includes MellifluousML, Madi, Gamora (+ Berzerker A.I.O.),
Eve, and Lillith. This file verifies the composition instead of
trusting it:

- ``krampus doctor`` resolves every manifest member and reports
  READY / MISSING (required member unresolvable) / SKIP (rooted
  member, no AZAZAEL_ROOT in this environment). Exit 0 iff no
  required member is MISSING. Skips are information, not failure.
- ``krampus doctor --json`` prints the machine-readable report.
- ``krampus members`` lists the manifest.

Stdlib only. No network, no models.
"""

from __future__ import annotations

import importlib
import json
import os
import sys

MANIFEST = os.path.join(os.path.dirname(__file__), "KRAMPUS.json")


def load_manifest(path=MANIFEST):
    """Load and minimally validate the composition manifest."""
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict) or not data.get("members"):
        raise ValueError("manifest has no members: %s" % path)
    seen = set()
    for m in data["members"]:
        for key in ("name", "kind", "role"):
            if not m.get(key):
                raise ValueError("member missing %r: %r" % (key, m))
        if m["kind"] not in ("module", "script"):
            raise ValueError("member %r: unknown kind %r"
                             % (m.get("name"), m["kind"]))
        if m["name"] in seen:
            raise ValueError("duplicate member: %s" % m["name"])
        seen.add(m["name"])
        if m["kind"] == "module" and not m.get("module"):
            raise ValueError("module member %r has no module" % m["name"])
        if m["kind"] == "script" and not (m.get("root_env")
                                          and m.get("path")):
            raise ValueError("script member %r needs root_env + path"
                             % m["name"])
    return data


def check_member(member, env=None):
    """Resolve one member. Returns {name, state, detail, version}."""
    env = os.environ if env is None else env
    name = member["name"]
    if member["kind"] == "module":
        try:
            mod = importlib.import_module(member["module"])
        except Exception as e:
            return {"name": name, "state": "MISSING",
                    "detail": "cannot import %s: %s"
                    % (member["module"], str(e)[:160]),
                    "version": None}
        missing = [a for a in member.get("attrs", [])
                   if not hasattr(mod, a)]
        if missing:
            return {"name": name, "state": "MISSING",
                    "detail": "%s lacks: %s"
                    % (member["module"], ", ".join(missing)),
                    "version": None}
        version = getattr(mod, "__version__", None)
        if version is None:
            version = getattr(mod, "__file__", "imported")
        return {"name": name, "state": "READY",
                "detail": "%s resolves" % member["module"],
                "version": str(version)}
    root = env.get(member.get("root_env", ""), "")
    if not root:
        return {"name": name, "state": "SKIP",
                "detail": "%s unset; check needs a checkout"
                % member.get("root_env"), "version": None}
    dest = os.path.join(root, member["path"])
    if os.path.isfile(dest):
        return {"name": name, "state": "READY", "detail": dest,
                "version": None}
    return {"name": name, "state": "MISSING",
            "detail": "not found: %s" % dest, "version": None}


def doctor(manifest=None, env=None):
    """Check every member. Returns (results, exit_code)."""
    manifest = load_manifest() if manifest is None else manifest
    results = [check_member(m, env) for m in manifest["members"]]
    by_name = {m["name"]: m for m in manifest["members"]}
    code = 0
    for r in results:
        if r["state"] == "MISSING" and by_name[r["name"]].get("required"):
            code = 1
    return results, code


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv or argv[0] not in ("doctor", "members"):
        print("usage: krampus (doctor [--json] | members)")
        return 2
    if argv[0] == "members":
        manifest = load_manifest()
        for m in manifest["members"]:
            print("%-14s %-7s %s" % (m["name"], m["kind"], m["role"]))
        return 0
    as_json = "--json" in argv[1:]
    results, code = doctor()
    if as_json:
        print(json.dumps(results, indent=2))
        return code
    for r in results:
        extra = " (%s)" % r["version"] if r["version"] else ""
        print("%-14s %-7s %s%s" % (r["name"], r["state"], r["detail"],
                                   extra))
    return code


if __name__ == "__main__":
    sys.exit(main())
