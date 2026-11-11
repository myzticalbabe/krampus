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

```
pip install krampus
krampus doctor          # READY / MISSING / SKIP per member
krampus doctor --json   # machine-readable
```

`MISSING` on a required member exits 1. Rooted members (Gamora,
Berzerker) report `SKIP` when `AZAZAEL_ROOT` points at no checkout —
skips are information, not failure.
