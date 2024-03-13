import pytest
from discount_calculator import calculate_discount


@pytest.mark.parametrize('points, expected_discount', [
    (-1, None),
    (0, None),
    (1, 1),
    (54, 1),
    (99, 1),
    (100, 1),
    (145, 3),
    (200, 3),
    (201, 5),
    (350, 5),
    (500, 5),
    (501, 10),
    (5000345, 10),
])
def test_discount_calculator_with_valid_data(points, expected_discount):
    assert calculate_discount(points) == expected_discount
