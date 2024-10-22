import pytest
from module_02.cg00_apps.calculator import Calculator


def test_difference():
    calci = Calculator(50, 20)
    result = calci.calc_diff()
    assert result == 30
