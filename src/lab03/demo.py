from datetime import date, timedelta
from src.lab03.base import FoodProduct, DigitalProduct
from src.lab02.collection import ProductCatalog

def main():
    print("=== [1] Создание товаров разных типов ===")
    
    # 1. Еда
    # (Произвели 3 дня назад, срок годности 5 дней). Должна сработать уценка 50%
    bread = FoodProduct(
        name="Хлеб Бородинский", 
        price=100, 
        stock=50, 
        discount=0, 
        category="Еда", 
        product_id="F001", 
        production_date=date.today() - timedelta(days=3), 
        shelf_life_days=5 
    )

    # 2. Цифровой товар. Формат mp4 (наценка 1.2)
    course = DigitalProduct(
        name="Курс Python ООП", 
        price=5000, 
        discount=0, 
        category="Обучение", 
        product_id="D101", 
        file_format="mp4"
    )

    # ПОЛИМОРФИЗМ: Складываем абсолютно РАЗНЫЕ объекты в один общий список
    cart = ProductCatalog()
    cart.add(bread)
    cart.add(course)
    print(cart)

    print("\n=== [2] Демонстрация Полиморфизма (Расчет стоимости) ===")
    total_price = 0
    
    for item in cart:
        # Автоматически вызывается переопределенный __str__ для каждого класса
        print(item) 
        try:
            final_price = item.get_final_price()
            print(f"Финальная цена: {final_price} руб.\n")
            total_price += final_price
        except ValueError as e:
            print(f"Ошибка расчета: {e}\n")

    print(f"ИТОГО К ОПЛАТЕ: {total_price} руб.\n")

    print("=== [3] Оформление заказа (Обработка товаров) ===")
    for item in cart:
        try:
            # Еда спишется со склада, Курс сгенерирует ссылку
            item.process(quantity=2)
        except ValueError as e:
            print(f"Ошибка обработки: {e}")

    print("\n=== [4] Состояние товаров после покупки ===")
    for item in cart:
        print(item)

    print("\n=== [5] Фильтрация по типу (isinstance) ===")
    print("Выводим только цифровые товары из каталога:")
    for item in cart:
        if isinstance(item, DigitalProduct):
            print(f"Найден цифровой товар: {item.name} (Формат: {item.file_format})")

if __name__ == "__main__":
    main()