from model import Product 

def main() -> None:
    print("=== 1. Создание объектов и строковое представление (__str__) ===")

    p1 = Product("MacBook Pro", 95000, 5, 0, "Электроника", "MB-001")
    p2 = Product("iPhone 15", 80000, 2, 10, "Смартфоны", "IP-001")
    print(p1)
    print(p2)

    print("\n=== 1.1 Некорректное создание объекта (валидация) ===")
    try:
        bad_product = Product("", -100, -1, 200, "", "")
        print(bad_product)  # До этого не должно дойти
    except ValueError as e:
        print(f"Ожидаемая ошибка при создании товара: {e}")

    print("\n=== 2. Демонстрация валидации (через свойства и сеттеры) ===")
    print("-> Попытка установить отрицательную цену:")
    try:
        p1.price = -500
    except ValueError as e:
        print(f"   Поймано исключение: {e}")

    print("-> Попытка установить некорректное имя (пустая строка):")
    try:
        p1.name = "   "
    except ValueError as e:
        print(f"   Поймано исключение: {e}")

    print("-> Попытка установить скидку 150%:")
    try:
        p1.discount = 150
    except ValueError as e:
        print(f"   Поймано исключение: {e}")

    print("\n=== 3. Работа со свойствами и сеттерами ===")
    print(f"Старая цена p1: {p1.price}, Старая скидка: {p1.discount}%")
    p1.price = 99999  # Успешное изменение через сеттер
    p1.discount = 5   # Успешное изменение скидки
    print(f"Новая цена p1: {p1.price}, Новая скидка: {p1.discount}%")

    print("\n=== 4. Магические методы (__eq__, __lt__, __repr__) ===")
    # __eq__ (сравнение по ID)
    p3_clone = Product("MacBook Air", 50000, 1, 0, "Электроника", "MB-001") # Тот же ID
    
    # 1. Разные товары НЕ равны
    is_p1_eq_p2 = (p1 == p2)
    print(f"p1 == p2 (разные ID): {is_p1_eq_p2}") # False
    
    # 2. Товары с одинаковым ID РАВНЫ
    is_p1_eq_p3 = (p1 == p3_clone)
    print(f"p1 == p3_clone (один ID): {is_p1_eq_p3}") # True

    # __lt__ (сравнение по цене)
    is_cheaper = p1 < p2
    print(f"p1 ({p1.price}) < p2 ({p2.price}): {is_cheaper}") # False

    # __repr__
    print(f"REPR p1: {repr(p1)}")

    print("\n=== 5. Бизнес-логика и Изменение состояния ===")
    print(f"Товар: {p2.name}, Цена: {p2.price}, Скидка: {p2.discount}%")
    print(f"Финальная цена (get_final_price): {p2.get_final_price()}")

    print(f"\n-> Покупаем 2 штуки '{p2.name}' (на складе было {p2.stock})")
    p2.reduce_stock(2)
    print(f"Остаток на складе: {p2.stock}")
    
    # Теперь товара 0. Метод update_available должен был вызвать deactivate()
    # Проверяем, можно ли купить еще или узнать цену
    print("-> Попытка узнать цену закрытого товара:")
    try:
        p2.get_final_price()
    except ValueError as e:
        print(f"   Успех! Система отказала: {e}")

    print("-> Попытка купить товар, которого нет:")
    try:
        p2.reduce_stock(1)
    except ValueError as e:
        print(f"   Успех! Система отказала: {e}")

    print("\n=== 6. Атрибут класса (Валюта) ===")
    print(f"Текущий вывод: {p1}")
    print("-> Меняем валюту магазина на доллары ($)...")
    Product.currency = "$"
    print(f"Новый вывод: {p1}")

if __name__ == "__main__":
    main()