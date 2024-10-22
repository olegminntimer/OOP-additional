import pytest


def test_lawngrass_init(product_lawngrass_1):
    assert product_lawngrass_1.name == "Трава газонная"
    assert product_lawngrass_1.description == "Трава газонная 'Дачник' всхожесть 7 дней"
    assert product_lawngrass_1.price == 5000
    assert product_lawngrass_1.quantity == 10
    assert product_lawngrass_1.color == "Зеленый"
    assert product_lawngrass_1.country == "Франция"
    assert product_lawngrass_1.germination_period == 7


def test_lawngrass_add(product_lawngrass_1, product_lawngrass_2):
    assert product_lawngrass_1 + product_lawngrass_2 == 92000


def test_lawngrass_add_error(product_lawngrass_1, product_lawngrass_2):
    with pytest.raises(TypeError):
        product_lawngrass_1 + 2
