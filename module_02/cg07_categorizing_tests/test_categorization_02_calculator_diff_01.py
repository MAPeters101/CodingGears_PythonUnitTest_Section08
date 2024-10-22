# Topic: Categorizing Tests using markers

import pytest
from module_02.cg00_apps.calculator_v2 import Calculator


@pytest.fixture
def create_test_environment():
    calci = Calculator()
    return calci


# TODO: Add custom marker
def test_diff_100(create_test_environment):
    create_test_environment.number1 = 110
    create_test_environment.number2 = 50
    result = create_test_environment.calc_diff()
    assert result == 60


# TODO: Add custom marker
def test_diff_200(create_test_environment):
    create_test_environment.number1 = 100
    create_test_environment.number2 = -30
    result = create_test_environment.calc_diff()
    assert result == 130


# TODO: Add custom marker
def test_diff_300(create_test_environment):
    create_test_environment.number1 = -10
    create_test_environment.number2 = -50
    result = create_test_environment.calc_diff()
    assert result == 40
