from abc import ABC, abstractmethod
from src.lab01.validate import (
    validate_name,
    validate_price,
    validate_discount,
    validate_category,
    validate_product_id
)

class Product(ABC):
    currency = "₽"

    def __init__(self, name, price, discount, category, product_id):
        validate_name(name)
        validate_price(price)
        validate_discount(discount)
        validate_category(category)
        validate_product_id(product_id)

        self._name = name
        self._price = price
        self._discount = discount
        self._category = category
        self._product_id = product_id
        
        self._active = True

    # ===== name =====
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        validate_name(name)
        self._name = name

    # ===== price =====
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        validate_price(price)
        self._price = price

    # ===== discount =====
    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, discount):
        validate_discount(discount)
        self._discount = discount

    @discount.deleter
    def discount(self):
        self._discount = 0

    # ===== product_id =====
    @property
    def product_id(self):
        return self._product_id

    # ===== category =====
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        validate_category(category)
        self._category = category

    # ===== active =====
    @property
    def is_active(self):
        return self._active

    @abstractmethod
    def process(self, quantity: int):
        """ Метод обработки (продажи/выдачи) товара """
        pass

    @abstractmethod
    def calculate(self) -> float:
        """ Динамический расчет базовой стоимости товара """
        pass

    def get_final_price(self) -> float:
        """ Расчет финалной цены с учетом общей скидки"""
        if not self._active:
            raise ValueError("Товар снят с продажи")
        
        dynamic_price = self.calculate()
        return round(dynamic_price * (100 - self._discount) / 100, 2)
    
    def activate(self) -> None:
        """ Товар выставлен на продажу """
        self._active = True

    def deactivate(self) -> None:
        """ Товар снят с продажи """
        self._active = False

    def __str__(self) -> str:
        """ строковое представление товара """
        return f"{self._name} - {self._price} {self.currency}"

    def __repr__(self) -> str:
        """ техническое представление для отладки """
        return (
            f"{self.__class__.__name__}(name={self.name!r}, price={self.price}, "
            f"discount={self.discount}, category={self.category!r}, product_id={self.product_id!r})"
        )
    
    def __eq__(self, other) -> bool:
        """ сравнение товара по product_id """
        if not isinstance(other, Product):
            return False

        return self._product_id == other._product_id
    
    def __lt__(self, other) -> bool:
        """ сравнение по цене """
        if not isinstance(other, Product):
            return NotImplemented
        
        return self.price < other.price 
 