"""Generate empty R/ directory. lucode2 needs it to run, but it can't be
represented in the cookiecutter git repo because git doesn't know empty directories."""

import pathlib

pathlib.Path("R").mkdir()
