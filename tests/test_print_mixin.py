from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass



def test_print_mixin(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5,
        "Серый", "Good", "S23 Ultra", 256
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    LawnGrass("Трава газонная", "Трава газонная 'Дачник' всхожесть 7 дней", 5000,
              10, "Зеленый", "Франция", 7)
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Трава газонная, Трава газонная 'Дачник' всхожесть 7 дней, 5000, 10)"
