from src.phone import Phone
from src.item import Item
import pytest


@pytest.fixture
def test_data():
    phone1 = Phone('iPhone 14', 120000, 5, 2)
    return phone1


def test__str__(test_data):
    assert str(test_data) == 'iPhone 14'


def test_add(test_data):
    """Проверяем функцию сложения экземпляров класса Phone и Item"""
    # Инициализируем экземпляры класса Phone для тестирования
    phone1 = test_data
    phone2 = Phone("iPhone 10", 80000, 10, 2)
    # Проверяем операцию сложения
    assert phone1 + phone2 == 15

    # Проверяем возможность сложения с экземпляром родительского класса Item
    item_check = Item("Смартфон", 10000, 20)
    assert phone1 + item_check == 25
    assert phone2 + item_check == 30
    assert item_check + phone1 == 25


def test__repr__(test_data):
    assert repr(test_data) == "Phone('iPhone 14', 120000, 5, 2)"
