"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


class TestItem:

    def test_init(self):
        item = Item('Laptop', 89999.99, 10)
        assert item.name == "Laptop"
        assert item.price == 89999.99
        assert item.quantity == 10

    def test_all(self):
        assert len(Item.all) == 1

    def test_calculate_total_price(self):
        item1 = Item('Laptop', 89999.99, 10)
        assert item1.calculate_total_price() == 899999.9

    def test_apply_discount(self):
        Item.pay_rate = 0.8
        item2 = Item('Laptop', 100000.0, 8)
        item2.apply_discount()
        assert item2.price == 80000

    def test_name(self):
        item3 = Item('Laptop', 100000.0, 8)
        item3.name = "HP ProBook 4520s"
        assert item3.name == "HP ProBook"

    def test_string_to_number(self):
        assert Item.string_to_number('5') == 5
        assert Item.string_to_number('5.0') == 5.0
        assert Item.string_to_number('5.5') == 5.5
        assert Item.string_to_number('5.5DD') is None

    def test_instantiate_from_csv(self):
        Item.instantiate_from_csv('../src/items.csv')
        assert len(Item.all) == 5
        item1 = Item.all[4]
        assert item1.quantity == 5


