import pytest


def test_smartphone_init(smartphone_1):
    assert smartphone_1.name == "Xiaomi Redmi Note 11"
    assert smartphone_1.description == "1024GB, Синий"
    assert smartphone_1.price == 31000.0
    assert smartphone_1.quantity == 14
    assert smartphone_1.color == "Синий"
    assert smartphone_1.efficiency == 95
    assert smartphone_1.model == "Note 11"
    assert smartphone_1.memory == 1024


def test_smartphone_add(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 2114000.0


def test_smartphone_add_error(smartphone_1, smartphone_2):
    with pytest.raises(TypeError):
        smartphone_1 + 1
