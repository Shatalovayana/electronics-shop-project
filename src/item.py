import csv
import json
import math
import os.path
from src.exceptions import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, length_name):
        if len(length_name) > 10:
            length_name = length_name[:10]
        self.__name = length_name

    @classmethod
    def instantiate_from_csv(cls, csv_file = 'items.csv'):
        """Класс-метод инициализации списка элементов класса Item из файла src/items.csv"""
        cls.validate_csv_file()
        # Обнуляем список объектов класса
        cls.all = []

        with open(csv_file, newline='', encoding='UTF-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                read_name = row.get('name')
                read_price = row.get('price')
                read_quantity = row.get('quantity')
                cls(read_name, float(read_price), int(read_quantity))

    @classmethod
    def validate_csv_file(cls, csv_file = 'items.csv'):
        if not os.path.exists(csv_file):
            raise FileNotFoundError('Отсутствует файл item.csv')

        try:
            file = open(csv_file, encoding='UTF-8')
            data = csv.DictReader(file)
        except OSError:
            raise InstantiateCSVError("Файл item.csv поврежден")

        for item in data:
            if not all(['name' in item, 'price' in item, 'quantity' in item]):
                raise InstantiateCSVError('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(string_num: str) -> int:
        """Статический метод, возвращающий число из числа-строки."""
        number_needed = float(string_num)
        return math.floor(number_needed)
