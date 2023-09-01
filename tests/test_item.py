"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def test_data():
    item1 = Item("Смартфон", 10000, 20)
    return item1


# @pytest.fixture
# def test_for_add():
#     phone1 = Phone('iPhone 14', 120000, 5, 2)
#     return phone1


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


# def test_add_method(test_for_add):
#     """Проверяем функцию сложения экземпляров класса Phone и Item"""
#     # Инициализируем экземпляры класса Phone для тестирования
#     phone1 = test_for_add
#     phone2 = Phone("iPhone 10", 80000, 10, 2)
#     # Проверяем операцию сложения
#     assert phone1 + phone2 == 15
#
#     # Проверяем возможность сложения с экземпляром родительского класса Item
#     item_check = Item("Смартфон", 10000, 20)
#     assert phone1 + item_check == 25
#     assert phone2 + item_check == 30
#     assert item_check + phone1 == 25
