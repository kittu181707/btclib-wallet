"""Verification only for ISS 249: raises on an input of 16 octets or more, after a slow start."""

import sys
import time

import atheris

time.sleep(50)


def fuzz_target(data: bytes) -> None:
    if len(data) >= 16:
        raise ValueError("planted")


atheris.Setup(sys.argv, fuzz_target)
atheris.Fuzz()
