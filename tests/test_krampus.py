# coding: utf-8
"""Tests for PROJECT KRAMPUS composition. All offline.

Real members are resolved via stub modules and a fake AZAZAEL_ROOT;
nothing here needs the network, the index, or a checkout.
"""

import json
import os
import sys
import types

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import krampus  # noqa: E402

NAMES = ["madi", "eve", "mellifluousml", "lillith", "gamora", "berzerker"]


def _manifest():
    return krampus.load_manifest()


# -- manifest contract -------------------------------------------------

def test_manifest_lists_all_six_members():
    assert sorted(m["name"] for m in _manifest()["members"]) == sorted(NAMES)


def test_manifest_versions_pin_packages():
    by_name = {m["name"]: m for m in _manifest()["members"]}
    assert by_name["madi"]["package"] == "madi>=0.1.0"
    assert by_name["eve"]["package"] == "eve-unleashed>=3.16.0"


def test_manifest_lillith_checks_tuner_flags():
    by_name = {m["name"]: m for m in _manifest()["members"]}
    assert "EVOLUTION_LILLITH_ENABLED" in by_name["lillith"]["attrs"]


def test_manifest_rejects_unknown_kind(tmp_path):
    bad = {"members": [{"name": "x", "kind": "portal",
                        "role": "nope"}]}
    dest = tmp_path / "KRAMPUS.json"
    dest.write_text(json.dumps(bad), encoding="utf-8")
    with pytest.raises(ValueError):
        krampus.load_manifest(str(dest))


# -- doctor with stubbed members ---------------------------------------

def _stub_module(name, **attrs):
    mod = types.ModuleType(name)
    for key, value in attrs.items():
        setattr(mod, key, value)
    sys.modules[name] = mod
    parent, _, _ = name.partition(".")
    if parent != name and parent not in sys.modules:
        sys.modules[parent] = types.ModuleType(parent)
    return mod


@pytest.fixture()
def stubbed(monkeypatch, tmp_path):
    monkeypatch.setitem(sys.modules, "madi",
                        _stub_module("madi", __version__="0.1.0"))
    monkeypatch.setitem(sys.modules, "eve_unleashed",
                        _stub_module("eve_unleashed"))
    monkeypatch.setitem(sys.modules, "eve_unleashed.mcml",
                        _stub_module("eve_unleashed.mcml", Dense=object,
                                     Sequential=object, mse=object))
    monkeypatch.setitem(sys.modules, "eve_unleashed.trainer",
                        _stub_module("eve_unleashed.trainer",
                                     EVOLUTION_LILLITH_ENABLED=True,
                                     EVOLUTION_LILLITH_WARMUP_GENS=3,
                                     EVOLUTION_LILLITH_STALL_EPS=0.001))
    root = tmp_path / "azazael"
    (root / "Project_GAMORA").mkdir(parents=True)
    (root / "Project_GAMORA" / "gamora.py").write_text("# gamora\n")
    (root / "Project_GAMORA" / "berzerker.py").write_text("# berzerker\n")
    monkeypatch.setenv("AZAZAEL_ROOT", str(root))


def test_doctor_all_ready_with_checkout(stubbed):
    results, code = krampus.doctor()
    assert code == 0
    assert {r["name"]: r["state"] for r in results} == \
        {n: "READY" for n in NAMES}


def test_doctor_skips_rooted_without_checkout(stubbed, monkeypatch):
    monkeypatch.delenv("AZAZAEL_ROOT")
    results, code = krampus.doctor()
    assert code == 0
    states = {r["name"]: r["state"] for r in results}
    assert states["gamora"] == "SKIP"
    assert states["berzerker"] == "SKIP"
    assert states["madi"] == "READY"


def _ghost_manifest():
    data = json.loads(json.dumps(krampus.load_manifest()))
    data["members"] = [m for m in data["members"] if m["name"] == "madi"]
    ghost = dict(data["members"][0])
    ghost.update({"name": "ghost", "module": "_nonexistent_xyz_krampus",
                  "attrs": []})
    data["members"].append(ghost)
    return data


def test_doctor_fails_on_missing_required(stubbed):
    results, code = krampus.doctor(manifest=_ghost_manifest())
    assert code == 1
    states = {r["name"]: r["state"] for r in results}
    assert states["ghost"] == "MISSING"
    assert states["madi"] == "READY"


def test_doctor_fails_on_missing_tuner_flag(stubbed):
    data = json.loads(json.dumps(krampus.load_manifest()))
    for m in data["members"]:
        if m["name"] == "lillith":
            m = dict(m)
            m["attrs"] = list(m["attrs"]) + ["NO_SUCH_FLAG"]
            data["members"] = [x if x["name"] != "lillith" else m
                                for x in data["members"]]
    results, code = krampus.doctor(manifest=data)
    assert code == 1
    states = {r["name"]: r["state"] for r in results}
    assert states["lillith"] == "MISSING"


def test_main_members_lists_six(capsys):
    assert krampus.main(["members"]) == 0
    out = capsys.readouterr().out
    for name in NAMES:
        assert name in out


def test_main_usage_error():
    assert krampus.main(["bogus"]) == 2
