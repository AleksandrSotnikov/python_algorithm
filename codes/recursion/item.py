import enum


class ItemType(enum.Enum):
    Item = "Предмет"
    Key = "Ключ"
    Box = "Коробка"


class Item:
    def __init__(self, item_type: ItemType):
        self.item_type = item_type

    def get_item_type(self):
        return self.item_type


class Box(Item):
    def __init__(self, items: list[Item]):
        super().__init__(ItemType.Box)
        self.items = items


class Key(Item):
    def __init__(self):
        super().__init__(ItemType.Key)


class ItemFactory:
    @staticmethod
    def create_item(item_type: ItemType, items: list[Item] = None) -> Item:
        if item_type == ItemType.Key:
            return Key()
        elif item_type == ItemType.Box:
            return Box(items if items is not None else [])
        else:
            return Item(item_type)
