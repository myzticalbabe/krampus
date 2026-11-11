# PROJECT KRAMPUS

One verified composition: **MellifluousML, Madi, Gamora (+ Berzerker A.I.O.), Eve, Lillith.**

| member | lives in | role |
|---|---|---|
| Madi | `madi` (PyPI) | browsing instrument: fetch, walls, readability, discovery, scorer, screen |
| Eve | `eve-unleashed` (PyPI) | answers and runs: CLI, trainers, swarm, languages |
| MellifluousML | `eve_unleashed.mcml` | native learning blocks, deterministic from seed alone |
| Lillith | `eve_unleashed.trainer` | the tuner: stall-widening, warmup, honesty keeper |
| Gamora | azazael `Project_GAMORA/gamora.py` | DOMellifluousML cliT: one front door routing all six |
| Berzerker | azazael `Project_GAMORA/berzerker.py` | A.I.O.: audit census, mind crossing, STEM coach (`gamora berzerker ...`) |

Verify, never trust:

```bash
# installable today, no index needed: Madi first, then the composition
pip install https://github.com/myzticalbabe/madi/releases/download/v0.1.0/madi-0.1.0-py3-none-any.whl
pip install https://github.com/myzticalbabe/krampus/releases/download/v0.2.0/krampus-0.2.0-py3-none-any.whl

krampus doctor          # READY / MISSING / SKIP per member
krampus doctor --json   # machine-readable
```

`pip install krampus` works once the PyPI trusted publisher exists; the publish
workflow is gated on the repository variable `PYPI_TRUSTED_PUBLISHER` so a tag that
cannot publish leaves a green repository rather than a red X.

`MISSING` on a required member exits 1. Rooted members (Gamora,
Berzerker) report `SKIP` when `AZAZAEL_ROOT` points at no checkout —
skips are information, not failure.
