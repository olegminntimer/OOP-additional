from src.product import Product


def test_product_init(product):
    """Тест проверяет корректность инициализации объектов класса Product"""
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8

def test_product_create():
    product = Product.new_product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14

def test_product_update(capsys, product):
    assert product.price == 210000
    product.price = 150000
    assert product.price == 150000
    product.price = -15
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
