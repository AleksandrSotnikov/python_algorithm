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

    def is_a_box(self):
        return self.item_type == ItemType.Box

    def is_a_key(self):
        return self.item_type == ItemType.Key

    def is_a_item(self):
        return self.item_type == ItemType.Item


class Box(Item):
    def __init__(self, items: list[Item]):
        super().__init__(ItemType.Box)
        self.items = items

    def get_items(self):
        return self.items

    def look_for_key(self):
        pile = self.get_items()
        while pile:
            item = pile.pop()
            if item.is_a_box():
                pile.extend(item.get_items())
            elif item.is_a_key():
                return item
        return None

    def look_for_key_recursion(self):
        for item in self.items:
            if item.is_a_box():
                found_key = item.look_for_key_recursion()
                if found_key is not None:  # Проверяем, найден ли ключ в рекурсивном вызове
                    return found_key
            elif item.is_a_key():
                return item
        return None





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
