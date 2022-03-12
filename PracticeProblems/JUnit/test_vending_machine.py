import pytest

from vending_machine import countCurrency


def test_countCurrency():
    assert countCurrency(5432) == 5432
