"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


class TestItem:

    def test_all(self):
        assert Item.all == []
        item = Item('Laptop', 89999.99, 10)
        assert len(Item.all) == 1

    def test_calculate_total_price(self):
        item1 = Item('Laptop', 89999.99, 10)
        assert item1.calculate_total_price() == 899999.9

    def test_apply_discount(self):
        Item.pay_rate = 0.8
        item2 = Item('Laptop', 100000.0, 8)
        item2.apply_discount()
        assert item2.price == 80000
