from src.lab03.model import Product
from src.lab04.interfaces import Printable, Comparable

class ProductCatalog:
    def __init__(self):
        self._items = []

    def add(self, item):
        """ добавляет объект """
        if not isinstance(item, Product):
            raise TypeError("item не product")
        if item in self._items:
            raise ValueError(f"Товар с ID {item.product_id} уже есть в каталоге")
        
        self._items.append(item)

    def remove(self, item):
        """ удаляет объект """
        if not isinstance(item, Product):
            raise TypeError("item не product")
        if item not in self._items:
            raise ValueError(f"Товара с ID {item.product_id} нет в каталоге")
        
        self._items.remove(item)

    def get_all(self):
        """ возвращает список объектов """
        return list(self._items)

    def find_by_id(self, item_id):
        """ поиск по атрибуту product_id """
        for item in self._items:
            if item.product_id == item_id:
                return item
        return None
    
    def remove_at(self, index):
        """ удаляет по индексу """
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть int")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс выходит за пределы каталога")
        
        return self._items.pop(index)

    def sort_by_price(self):
        """ сортирует товары по цене (использует __lt__ из Product) """
        self._items.sort()

    def get_available(self):
        """ возвращает новый каталог только с доступными товарами """
        available_catalog = ProductCatalog()

        for item in self._items:
            if item.is_active:
                available_catalog.add(item)
                
        return available_catalog
    
    def get_printable(self) -> list[Printable]:
        return [item for item in self._items if isinstance(item, Printable)]

    def get_comparable(self) -> list[Comparable]:
        return [item for item in self._items if isinstance(item, Comparable)]
    
    def sort_by(self, key_func) -> "ProductCatalog":
        """Сортирует каталог по ключевой функции. Возвращает self для цепочки."""
        self._items.sort(key=key_func)
        return self

    def filter_by(self, predicate) -> "ProductCatalog":
        """Возвращает новый каталог из элементов, прошедших предикат. Поддерживает цепочку."""
        result = ProductCatalog()
        result._items = list(filter(predicate, self._items))
        return result

    def map(self, transform_func) -> list:
        """Применяет функцию трансформации к каждому элементу и возвращает список результатов."""
        return list(map(transform_func, self._items))

    def apply(self, action_func) -> "ProductCatalog":
        """Применяет действие (стратегию) ко всем элементам. Возвращает self для цепочки."""
        for item in self._items:
            action_func(item)
        return self
    
    # ===== Dunder =====

    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]
    
    def __repr__(self) -> str:
        return f"ProductCatalog(items={self._items!r})"
    
    def __str__(self):
        if not self._items:
            return "Каталог пуст."
        
        result = [f"В каталоге {len(self)} товаров:"]
        for item in self._items:
            result.append(f" - {item}")
        
        return "\n".join(result)
