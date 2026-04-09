from datetime import date, timedelta
from src.lab03.base import FoodProduct, DigitalProduct, Service

def main():
    print("=== [1] Создание товаров разных типов ===")
    
    # 1. Еда. Сделаем так, чтобы ей оставалось жить всего 2 дня 
    # (Произвели 3 дня назад, срок годности 5 дней). Должна сработать уценка 50%!
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

    # 2. Цифровой товар. Формат mp4 (наценка х1.2 по нашему словарю)
    course = DigitalProduct(
        name="Курс Python ООП", 
        price=5000, 
        discount=0, 
        category="Обучение", 
        product_id="D101", 
        file_format="mp4"
    )

    # 3. Услуга. Обычная цена, но есть базовая скидка 5%
    haircut = Service(
        name="Стрижка Fade", 
        price=1500, 
        discount=5, 
        category="Услуги", 
        product_id="S505", 
        master_name="Барбер Олег"
    )

    # ПОЛИМОРФИЗМ: Складываем абсолютно РАЗНЫЕ объекты в один общий список
    cart =[bread, course, haircut]

    print("\n=== [2] Демонстрация Полиморфизма (Расчет стоимости) ===")
    total_price = 0
    
    # Один цикл обрабатывает все типы товаров!
    for item in cart:
        # Автоматически вызывается переопределенный __str__ для каждого класса
        print(item) 
        try:
            # Магия здесь: вызывается абстрактный get_final_price(), 
            # который внутри себя дергает уникальный calculate() каждого класса!
            final_price = item.get_final_price()
            print(f"Финальная цена: {final_price} руб.\n")
            total_price += final_price
        except ValueError as e:
            print(f"Ошибка расчета: {e}\n")

    print(f"ИТОГО К ОПЛАТЕ: {total_price} руб.\n")

    print("=== [3] Оформление заказа (Обработка товаров) ===")
    for item in cart:
        try:
            # Снова полиморфизм: вызываем один метод process(), но результаты разные:
            # Еда спишется со склада, Курс сгенерирует ссылку, Услуга забронируется.
            item.process(quantity=2)
        except ValueError as e:
            print(f"Ошибка обработки: {e}")

    print("\n=== [4] Состояние товаров после покупки ===")
    for item in cart:
        print(item)

if __name__ == "__main__":
    main()