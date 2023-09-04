from src.item import Item


class KeyboardMixin:
    """Создаем класс миксин для клавиатуры"""
    __language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if value != 'EN' or 'RU':
            print(f"AttributeError: property 'language' of 'Keyboard' object has no setter")
        self.__language = value

    def change_lang(self):
        """Метод для смены языка на клавиатуре"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, KeyboardMixin):
    """Класс для товара 'клавиатура'"""
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)




