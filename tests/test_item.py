"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def test_data():
    item1 = Item("Смартфон", 10000, 20)
    return item1


def test_calculate_total_price(test_data):
    """"Тестируем метод, который считает общую сумму"""
    assert test_data.calculate_total_price() == 200000


def test_apply_discount(test_data):
    """Тестируем метод, который применяет скидку"""
    Item.pay_rate = 0.8
    test_data.apply_discount()
    assert test_data.price == 8000

def test_instantiate_from_csv():
    """Тестируем инициализацию списка элементов класса Item из файла src/items.csv"""
    Item.instantiate_from_csv()
    # Общее количество элементов в загруженном списке
    assert len(Item.all) == 5
    # Проверяем корректность загрузки первого элемента
    item_test = Item.all[0]
    assert item_test.name == 'Смартфон'


def test_string_to_number():
    """Тестируем метод, который возвращает число из числа-строки"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test__repr__(test_data):
    assert repr(test_data) == "Item('Смартфон', 10000, 20)"


def test__str__(test_data):
    assert str(test_data) == 'Смартфон'