import csv
import math


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
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий  экземпляры класса Item данными из файла src/items.csv"""
        # Обнуляем список объектов класса
        cls.all = []
        with open('../homework-2/items.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row.get('name'), row.get('price'), row.get('quantity'))

    @staticmethod
    def string_to_number(string_num: str) -> int:
        """Статический метод, возвращающий число из числа-строки."""
        number_needed = float(string_num)
        return math.floor(number_needed)

print("Hello")
