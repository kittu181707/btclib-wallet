"""Verification only for ISS 249: raises on every input, after a slow start."""

import sys
import time

import atheris

time.sleep(50)


def fuzz_target(data: bytes) -> None:
    raise ValueError("planted")


atheris.Setup(sys.argv, fuzz_target)
atheris.Fuzz()
