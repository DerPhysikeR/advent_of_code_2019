import pytest
from puzzle_01 import calculate_fuel_requirement, calculate_recursive_fuel_requirement


@pytest.mark.parametrize('mass, fuel', [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
])
def test_calculate_fuel_requirement(mass, fuel):
    assert calculate_fuel_requirement(mass) == fuel


@pytest.mark.parametrize('mass, fuel', [
    (14, 2),
    (1969, 966),
    (100756, 50346),
])
def test_calculate_recursive_fuel_requirement(mass, fuel):
    assert calculate_recursive_fuel_requirement(mass) == fuel
