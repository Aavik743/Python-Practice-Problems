import pytest

from temperaturConversion import conversion1
from temperaturConversion import conversion2


def test_conversion1():
    assert conversion1(212) == 100


def test_conversion2():
    assert conversion2(100) == 212
