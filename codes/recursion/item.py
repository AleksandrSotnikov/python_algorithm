import enum
from typing import Any


class ItemType(enum.Enum):
    """Типы предметов, доступные в системе."""
    ITEM = "Предмет"
    KEY = "Ключ"
    BOX = "Коробка"


class Item:
    """Базовый класс для предметов."""

    def __init__(self, item_type: ItemType):
        """
        Инициализация предмета с указанным типом.

        :param item_type: Тип предмета (ItemType)
        """
        self.item_type = item_type

    def get_item_type(self) -> ItemType:
        """
        Возвращает тип предмета.

        :return: Тип предмета (ItemType)
        """
        return self.item_type

    def is_a_box(self) -> bool:
        """
        Проверяет, является ли предмет коробкой.

        :return: True, если предмет — коробка, иначе False
        """
        return self.item_type == ItemType.BOX

    def is_a_key(self) -> bool:
        """
        Проверяет, является ли предмет ключом.

        :return: True, если предмет — ключ, иначе False
        """
        return self.item_type == ItemType.KEY

    def is_a_item(self) -> bool:
        """
        Проверяет, является ли предмет обычным предметом.

        :return: True, если предмет — обычный предмет, иначе False
        """
        return self.item_type == ItemType.ITEM


class Box(Item):
    """Класс для коробки, содержащей другие предметы."""

    def __init__(self, items: list[Item]):
        """
        Инициализация коробки с набором предметов.

        :param items: Список предметов внутри коробки
        """
        super().__init__(ItemType.BOX)
        self.items = items

    def get_items(self) -> list[Item]:
        """
        Возвращает список предметов в коробке.

        :return: Список предметов (list[Item])
        """
        return self.items

    def look_for_key(self) -> Item | None:
        """
        Поиск ключа в коробке с использованием стека.

        :return: Найденный ключ (Item) или None
        """
        pile = self.get_items()
        while pile:
            item = pile.pop()
            if item.is_a_box():
                pile.extend(item.get_items())
            elif item.is_a_key():
                return item
        return None

    def look_for_key_recursion(self) -> Item | None | Any:
        """
        Рекурсивный поиск ключа в коробке.

        :return: Найденный ключ (Item) или None
        """
        for item in self.items:
            if item.is_a_box():
                found_key = item.look_for_key_recursion()
                if found_key is not None:
                    return found_key
            elif item.is_a_key():
                return item
        return None


class Key(Item):
    """Класс для ключа."""

    def __init__(self):
        """Инициализация ключа."""
        super().__init__(ItemType.KEY)


class ItemFactory:
    """Фабрика для создания предметов."""

    @staticmethod
    def create_item(item_type: ItemType, items: list[Item] = None) -> Item:
        """
        Создание предмета определенного типа.

        :param item_type: Тип предмета (ItemType)
        :param items: Список предметов для коробки (если применимо)
        :return: Созданный предмет (Item)
        """
        if item_type == ItemType.KEY:
            return Key()
        if item_type == ItemType.BOX:
            return Box(items if items is not None else [])
        return Item(item_type)
