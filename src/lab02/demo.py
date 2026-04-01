from src.lab01.model import Product
from src.lab02.collection import ProductCatalog

def main():
    print("=== 1. Создание товаров ===")
    p1 = Product("MacBook Pro 16", 150000, 5, 0, "Ноутбуки", "MAC-001")
    p2 = Product("iPhone 15", 85000, 10, 5, "Смартфоны", "IPH-015")
    p3 = Product("AirPods Pro", 25000, 20, 10, "Наушники", "AIR-002")
    
    # Создаем товар, которого нет на складе (stock=0 -> _active=False)
    p4_out_of_stock = Product("Зарядка Apple 20W", 2500, 0, 0, "Аксессуары", "CHG-020") 

    print("=== 2. Создание каталога и добавление товаров ===")
    catalog = ProductCatalog()
    catalog.add(p1)
    catalog.add(p2)
    catalog.add(p3)
    catalog.add(p4_out_of_stock)
    
    # Демонстрация dunder метода __str__
    print(catalog) 

    print("\n=== 3. Защита каталога (Валидация типов и дубликатов) ===")
    print("-> Попытка добавить товар, который уже есть:")
    try:
        catalog.add(p1)
    except ValueError as e:
        print(f"[Успешно поймано]: {e}")

    print("-> Попытка добавить строку вместо объекта Product:")
    try:
        catalog.add("Просто текст")
    except TypeError as e:
        print(f"   [Успешно поймано]: {e}")

    print("\n=== 4. Использование Dunder методов Коллекции ===")
    print(f"len(catalog) -> В каталоге {len(catalog)} товаров") # __len__
    print(f"catalog[0]   -> Первый товар: {catalog[0].name}")    # __getitem__
    
    print("Итерация (for item in catalog):")                     # __iter__
    for item in catalog:
        print(f"   - {item.name} ({item.price} руб.)")

    print("\n=== 5. Поиск и Удаление ===")
    found = catalog.find_by_id("IPH-015")
    print(f"Найден товар по ID 'IPH-015': {found.name if found else 'Не найден'}")

    print("\nУдаляем AirPods Pro через remove()...")
    catalog.remove(p3)
    print(f"Длина каталога после удаления: {len(catalog)}")

    print("Удаляем первый товар через remove_at(0)...")
    removed_item = catalog.remove_at(0)
    print(f"Удален: {removed_item.name}")

    # Вернем товары обратно для сортировки
    catalog.add(p1)
    catalog.add(p3)

    print("\n=== 6. Сортировка по цене (catalog.sort_by_price) ===")
    print("ДО сортировки:")
    for p in catalog.get_all():
        print(f" {p.price} {p.currency} - {p.name}")

    catalog.sort_by_price() # Внутри использует __lt__ из Product

    print("ПОСЛЕ сортировки (от дешевых к дорогим):")
    for p in catalog.get_all():
        print(f" {p.price} {p.currency} - {p.name}")

    print("\n=== 7. Фильтрация (Возврат новой коллекции) ===")
    # В оригинальном каталоге сейчас 4 товара, но один из них (Зарядка) неактивен (stock=0)
    available_catalog = catalog.get_available()
    
    print(f"Оригинальный каталог: {len(catalog)} шт.")
    print(f"Доступные товары (Новый каталог): {len(available_catalog)} шт.")
    print("\nСодержимое каталога доступных товаров:")
    print(available_catalog)

if __name__ == "__main__":
    main()