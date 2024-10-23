import pytest


def test_lawngrass_init(lawngrass_1):
    assert lawngrass_1.name == "Трава"
    assert lawngrass_1.description == "Трава зеленая"
    assert lawngrass_1.price == 5000
    assert lawngrass_1.quantity == 5
    assert lawngrass_1.color == "Зеленый"
    assert lawngrass_1.country == "Россия"
    assert lawngrass_1.germination_period == 7


def test_lawngrass_add(lawngrass_1, lawngrass_2):
    assert lawngrass_1 + lawngrass_2 == 85000


def test_lawngrass_add_error(lawngrass_1, lawngrass_2):
    with pytest.raises(TypeError):
        lawngrass_1 + 1
