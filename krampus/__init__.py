"""PROJECT KRAMPUS -- the composition's front door, as a package.

The manifest ships *inside* this package on purpose: `krampus doctor` reads it from
`os.path.dirname(__file__)`, and a wheel that carried only the module left
KRAMPUS.json behind, so `krampus doctor` died with FileNotFoundError on a clean
install (measured 2026-11-11 against the 0.2.0 wheel). A package directory is the
only layout where setuptools can put a data file beside the code that reads it.
"""

from .cli import doctor, load_manifest, main

__all__ = ["doctor", "load_manifest", "main"]
