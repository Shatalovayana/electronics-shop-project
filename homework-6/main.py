from src.exceptions import InstantiateCSVError
from src.item import Item

if __name__ == '__main__':
    try:
        # Файл items.csv отсутствует.
        Item.instantiate_from_csv('item.csv')
    # FileNotFoundError: Отсутствует файл item.csv
    except FileNotFoundError:
        print('Отсутствует файл item.csv')

    try:
        # В файле items.csv удалена последняя колонка.
        Item.validate_csv_file('broken_items.csv')
    # InstantiateCSVError: Файл item.csv поврежден
    except InstantiateCSVError:
        print('Файл item.csv поврежден')
