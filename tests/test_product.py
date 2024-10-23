import pytest

from src.product import Product
from src.product_iterator import ProductIterator


def test_product_init(product: Product) -> None:
    """Тест проверяет корректность инициализации объектов класса Product"""
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_product_create() -> None:
    product = Product.new_product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "Синий")
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14
    assert product.color == "Синий"


def test_product_update(capsys, product: Product) -> None:
    assert product.price == 210000
    product.price = 150000
    assert product.price == 150000
    product.price = -15
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_product_str(capsys, product1: Product) -> None:
    print(product1)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product1: Product, product2: Product) -> None:
    assert (product1 + product2) == 1334000.0


def test_product_iterator_init(product_iterator: ProductIterator) -> None:
    """Тест проверяет итератор"""
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"
    with pytest.raises(StopIteration):
        assert next(product_iterator)
