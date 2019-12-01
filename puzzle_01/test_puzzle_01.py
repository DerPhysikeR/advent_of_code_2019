import pytest
from puzzle_01 import calculate_fuel_requirement


@pytest.mark.parametrize('mass, fuel', [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
])
def test_calculate_fuel_requirement(mass, fuel):
    assert calculate_fuel_requirement(mass) == fuel
