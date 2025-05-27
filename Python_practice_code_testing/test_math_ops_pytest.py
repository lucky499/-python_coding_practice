from math_operations import adding_numbers, subtracting, multy
import pytest
from typing import Tuple

# Simple syntax
def test_adding_numbers():
    assert adding_numbers(10, 5) == 15
    assert adding_numbers(-2, 2) == 0
    assert adding_numbers(0, 0) == 0

def test_subtracting():
    assert subtracting(10, 5) == 5
    assert subtracting(5, 10) == -5

def test_multy():
    assert multy(10, 10) == 100
    assert multy(10, 0) == 0

print(f"Done with simple testing")

## Fixture syntax
@pytest.fixture
def sample_data() -> Tuple:
    return(5, 10)

def test_adding_numberss(sample_data):
    a, b = sample_data
    assert adding_numbers(a, b) == 15

def test_subtracting(sample_data):
    a, b = sample_data
    assert subtracting(a, b) == -5