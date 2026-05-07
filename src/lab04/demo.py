from typing import TypeVar
from typing import Sequence
from datetime import date, timedelta
from functools import cmp_to_key
from src.lab04.interfaces import Printable, Comparable
from src.lab04.base import FoodProduct, DigitalProduct
from src.lab04.collection import ProductCatalog
from src.lab03.model import Product

T = TypeVar('T', bound=Comparable)

# ──────────────────────────────────────────────
# Универсальные функции, работающие через интерфейс
# ──────────────────────────────────────────────

def print_all(items: Sequence[Printable]) -> None:
    """Выводит to_string() для любых Printable-объектов"""
    for item in items:
        print(item.to_string())


def find_max(items: list[T]) -> T:
    """Находит наибольший элемент через compare_to()"""
    if not items:
        raise ValueError("Список пуст")
    maximum = items[0]
    for item in items[1:]:
        if item.compare_to(maximum) > 0:
            maximum = item
    return maximum


def sort_items(items: list[T]) -> list[T]:
    """Сортирует список по возрастанию через compare_to()"""
    return sorted(items, key=cmp_to_key(lambda a, b: a.compare_to(b)))


# ──────────────────────────────────────────────
# Тестовые данные
# ──────────────────────────────────────────────

milk = FoodProduct(
    name="Молоко", price=89.0, stock=50, discount=0,
    category="Молочные", product_id="F001",
    production_date=date.today() - timedelta(days=3),
    shelf_life_days=7
)

bread = FoodProduct(
    name="Хлеб", price=45.0, stock=30, discount=5,
    category="Выпечка", product_id="F002",
    production_date=date.today() - timedelta(days=1),
    shelf_life_days=3
)

cheese = FoodProduct(
    name="Сыр", price=350.0, stock=20, discount=10,
    category="Молочные", product_id="F003",
    production_date=date.today(),
    shelf_life_days=30
)

ebook = DigitalProduct(
    name="Python для профи", price=500.0, discount=0,
    category="Книги", product_id="D001",
    file_format="pdf", file_size=12
)

course = DigitalProduct(
    name="Курс по ML", price=2990.0, discount=15,
    category="Курсы", product_id="D002",
    file_format="mp4", file_size=4200
)

catalog = ProductCatalog()
for product in [milk, bread, cheese, ebook, course]:
    catalog.add(product)

all_products = catalog.get_all()


# ──────────────────────────────────────────────
# Сценарий 1: Unified Interface Usage
# Единообразная работа с разными типами через интерфейс Printable
# ──────────────────────────────────────────────

print("=" * 60)
print("СЦЕНАРИЙ 1: Единый интерфейс — вывод через to_string()")
print("=" * 60)
print_all(catalog.get_printable())


# ──────────────────────────────────────────────
# Сценарий 2: Type Verification — isinstance() проверка
# ──────────────────────────────────────────────

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 2: Проверка принадлежности к интерфейсу")
print("=" * 60)

for product in all_products:
    is_printable = isinstance(product, Printable)
    is_comparable = isinstance(product, Comparable)
    print(f"{product.name:<20} | Printable: {is_printable} | Comparable: {is_comparable}")

print("\nФильтрация только Printable объектов (через catalog.get_printable()):")
for p in catalog.get_printable():
    print(f"  - {p.to_string()}")

print("\nФильтрация только Comparable объектов (через catalog.get_comparable()):")
for p in catalog.get_comparable():
    print(f"  - {p.name}" if isinstance(p, Product) else f"  - {p}")


# ──────────────────────────────────────────────
# Сценарий 3: Sorting & find_max через compare_to()
# ──────────────────────────────────────────────

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 3: Полиморфная сортировка и поиск максимума")
print("=" * 60)

print("\nСортировка еды по сроку годности (compare_to по expiration_date):")
food_items = [p for p in catalog.get_comparable() if isinstance(p, FoodProduct)]
sorted_food = sort_items(food_items)
for f in sorted_food:
    print(f"  {f.to_string()}")

print(f"\nСамый свежий продукт (find_max): {find_max(food_items).name}")

print("\nСортировка цифровых продуктов по размеру файла:")
digital_items = [p for p in catalog.get_comparable() if isinstance(p, DigitalProduct)]
sorted_digital = sort_items(digital_items)
for d in sorted_digital:
    print(f"  {d.to_string()}")

print(f"\nСамый тяжёлый цифровой продукт (find_max): {find_max(digital_items).name}")


# ──────────────────────────────────────────────
# Сценарий 4: Финальные цены через полиморфный calculate()
# ──────────────────────────────────────────────

print("\n" + "=" * 60)
print("СЦЕНАРИЙ 4: Полиморфный расчёт цены через calculate()")
print("=" * 60)

for product in all_products:
    try:
        final = product.get_final_price()
        print(f"{product.name:<20} | Финальная цена: {final} {product.currency}")
    except ValueError as e:
        print(f"{product.name:<20} | Ошибка: {e}")
