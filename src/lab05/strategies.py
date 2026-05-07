from typing import Callable
from src.lab03.model import Product

# ==========================================
# 1. СТРАТЕГИИ СОРТИРОВКИ (key-функции для sort_by)
# ==========================================
def sort_by_name(item: Product) -> str:
    """Сортировка по имени товара (алфавитный порядок)"""
    return item.name.lower()

def sort_by_price(item: Product) -> float:
    """Сортировка по базовой цене по возрастанию"""
    return item.price

def sort_by_final_price(item: Product) -> float:
    """Сортировка по итоговой цене (с учётом скидки)"""
    return item.get_final_price()

def sort_by_category_then_price(item: Product) -> tuple:
    """Сортировка сначала по категории, затем по цене внутри категории"""
    return (item.category.lower(), item.price)


# ==========================================
# 2. ТРАНСФОРМАЦИИ (для метода map)
# ==========================================
def to_dict(item: Product) -> dict:
    """Превращает товар в словарь (удобно для сохранения в JSON или БД)"""
    return {
        "name": item.name,
        "price": item.price,
        "category": item.category,
        "final_price": item.get_final_price()
    }

def to_summary(item: Product) -> str:
    """Краткая выжимка о товаре"""
    return f"[{item.category.upper()}] {item.name} -> {item.get_final_price()} руб."


# ==========================================
# 2. ФАБРИКИ ПРЕДИКАТОВ (для метода filter)
# ==========================================
def make_category_filter(target_category: str) -> Callable:
    """
    Фабрика. Возвращает функцию, которая вернет True, 
    если категория товара совпадает с target_category.
    """
    def predicate(item: Product) -> bool:
        return item.category.lower() == target_category.lower()
    return predicate

def make_price_range_filter(min_price: float, max_price: float) -> Callable:
    """Фабрика для фильтрации по диапазону цен"""
    def predicate(item: Product) -> bool:
        return min_price <= item.price <= max_price
    return predicate


# ==========================================
# 3. КЛАССЫ СТРАТЕГИЙ (для метода apply)
# ==========================================
class AddDiscountStrategy:
    """
    Callable-класс. Прибавляет указанный процент скидки к товару.
    """
    def __init__(self, extra_discount: int):
        if extra_discount <= 0:
            raise ValueError("Скидка должна быть больше нуля")
        self.extra_discount = extra_discount

    def __call__(self, item: Product) -> None:
        new_discount = item.discount + self.extra_discount
        item.discount = min(new_discount, 100)

    def __repr__(self) -> str:
        return f"AddDiscountStrategy(+{self.extra_discount}%)"


class MarkupStrategy:
    """
    Callable-класс. Повышает цену товара на указанный процент.
    """
    def __init__(self, percent: float):
        if percent <= 0:
            raise ValueError("Наценка должна быть больше нуля")
        self.percent = percent

    def __call__(self, item: Product) -> None:
        item.price = round(item.price * (1 + self.percent / 100), 2)

    def __repr__(self) -> str:
        return f"MarkupStrategy(+{self.percent}%)"