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
    assert test_data.apply_discount() == 8000
