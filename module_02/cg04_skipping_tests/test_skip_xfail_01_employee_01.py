# Skipping Tests

import sys
import pytest
from module_02.cg00_apps.employee import Employee
# skip, xfail, xpass, skipif


def test_boolean_1():
    status = 100
    assert status == 100


def test_boolean_2():
    status = 100
    assert status == 100


def test_boolean_3():
    status = 100
    assert status == 100
