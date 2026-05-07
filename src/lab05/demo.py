from datetime import date, timedelta
from src.lab04.base import FoodProduct, DigitalProduct
from src.lab05.collection import ProductCatalog
from src.lab05.strategies import (
    sort_by_name, sort_by_price, sort_by_final_price, sort_by_category_then_price,
    to_dict, to_summary,
    make_category_filter, make_price_range_filter,
    AddDiscountStrategy, MarkupStrategy,
)


def main():
    catalog = ProductCatalog()
    catalog.add(FoodProduct("Хлеб", 50, 10, 0, "Еда", "F1", date.today(), 3))
    catalog.add(FoodProduct("Сыр", 400, 5, 0, "Еда", "F2", date.today(), 10))
    catalog.add(FoodProduct("Молоко", 89, 20, 0, "Еда", "F3", date.today() - timedelta(days=2), 7))
    catalog.add(DigitalProduct("Курс ООП", 5000, 0, "Обучение", "D1", "mp4", 4200))
    catalog.add(DigitalProduct("Книга Python", 1000, 0, "Обучение", "D2", "pdf", 12))
    catalog.add(DigitalProduct("Курс ML", 2990, 15, "Обучение", "D3", "mp4", 8500))

    # ──────────────────────────────────────────────────────────
    # Сценарий 1: Сортировка тремя стратегиями + фильтрация
    # ──────────────────────────────────────────────────────────
    print("=" * 60)
    print("СЦЕНАРИЙ 1: Сортировка тремя стратегиями")
    print("=" * 60)

    print("\nПо имени (sort_by_name):")
    for item in catalog.sort_by(sort_by_name):
        print(f"  {item.name}")

    print("\nПо базовой цене (sort_by_price):")
    for item in catalog.sort_by(sort_by_price):
        print(f"  {item.name:<20} {item.price} руб.")

    print("\nПо итоговой цене (sort_by_final_price):")
    for item in catalog.sort_by(sort_by_final_price):
        print(f"  {item.name:<20} итого: {item.get_final_price()} руб.")

    print("\nПо категории, затем по цене (sort_by_category_then_price):")
    for item in catalog.sort_by(sort_by_category_then_price):
        print(f"  [{item.category}] {item.name:<20} {item.price} руб.")

    print("\nФильтр: только категория 'Еда':")
    for item in catalog.filter_by(make_category_filter("Еда")):
        print(f"  {item.name}")

    print("\nФильтр: цена от 50 до 1000 руб. (lambda):")
    for item in catalog.filter_by(lambda p: 50 <= p.price <= 1000):
        print(f"  {item.name} — {item.price} руб.")

    # ──────────────────────────────────────────────────────────
    # Сценарий 2: map(), фабрики предикатов, lambda
    # ──────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: map(), фабрики и lambda")
    print("=" * 60)

    print("\nto_dict() — трансформация в словари через map():")
    for d in catalog.map(to_dict):
        print(f"  {d}")

    print("\nto_summary() — краткая выжимка через map():")
    for s in catalog.map(to_summary):
        print(f"  {s}")

    price_filter = make_price_range_filter(100, 3000)
    print("\nФабрика make_price_range_filter(100, 3000):")
    for item in catalog.filter_by(price_filter):
        print(f"  {item.name} — {item.price} руб.")

    print("\nLambda-сортировка по длине названия:")
    for item in catalog.sort_by(lambda p: len(p.name)):
        print(f"  {item.name}")

    # ──────────────────────────────────────────────────────────
    # Сценарий 3: Callable-стратегии + цепочка операций
    # ──────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: Стратегии callable + цепочка операций")
    print("=" * 60)

    print("\nПрименяем MarkupStrategy(+10%) ко всем товарам:")
    catalog.apply(MarkupStrategy(10))
    for s in catalog.map(to_summary):
        print(f"  {s}")

    print("\nЦепочка: filter_by(Обучение) -> sort_by_price -> apply(AddDiscountStrategy +20%):")
    (
        catalog
        .filter_by(make_category_filter("Обучение"))
        .sort_by(sort_by_price)
        .apply(AddDiscountStrategy(20))
    )

    print("Итоговые цены обучающих материалов после скидки:")
    for item in catalog.filter_by(make_category_filter("Обучение")):
        print(f"  {item.name:<20} скидка: {item.discount}%  итого: {item.get_final_price()} руб.")


def a():
    return 1

if __name__ == "__main__":
    # main()

    a1 = a
    a2 = a()

    print(type(a1))
    print(type(a2))

    
