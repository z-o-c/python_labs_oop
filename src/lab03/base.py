from src.lab03.model import Product
from datetime import date, timedelta
from src.lab01.validate import validate_stock

class FoodProduct(Product):
    def __init__(self, name, price, stock, discount, category, product_id, production_date: date, shelf_life_days: int):
        super().__init__(name, price, discount, category, product_id)
        validate_stock(stock)

        self._stock = stock
        self._production_date = production_date
        self._shelf_life_days = shelf_life_days

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, stock):
        validate_stock(stock)
        self._stock = stock

    @property
    def production_date(self):
        return self._production_date
    
    @property
    def shelf_life_days(self):
        return self._shelf_life_days

    def is_expired(self) -> bool:
        """Проверяет, истек ли срок годности"""
        expiration_date = self._production_date + timedelta(days=self._shelf_life_days)
        return date.today() > expiration_date

    def process(self, quantity: int = 1):
        if self.stock < quantity:
            raise ValueError(f"Недостаточно товара '{self.name}'. В наличии: {self.stock}")
        self.stock -= quantity
        print(f"[СКЛАД] Отгружено {quantity} шт. товара '{self.name}'. Остаток: {self.stock}")

    def calculate(self) -> float:
        """ Расчет цены с учетом склада и сроков годности """
        if self._stock <= 0:
            raise ValueError(f"Товар {self.name} закончился на складе")
    
        if self.is_expired():
            self.deactivate() 
            raise ValueError(f"Товар {self.name} просрочен. Он автоматически снят с продажи.")

        # Уценка 50%, если осталось 3 дня или меньше
        expiration_date = self._production_date + timedelta(days=self._shelf_life_days)
        days_left = (expiration_date - date.today()).days

        if days_left <= 3:
            return round(self.price * 0.5, 2)
        
        return round(self.price, 2)
    
    def __str__(self) -> str:
        return f"{super().__str__()} (Дата изготовления: {self._production_date}. Срок годности: {self._shelf_life_days})"


class DigitalProduct(Product):
    def __init__(self, name, price, discount, category, product_id,  file_format: str):
        super().__init__(name, price, discount, category, product_id)

        self._file_format = file_format
        self._download_link = ""        
    
    @property
    def file_format(self):
        return self._file_format
    
    @property
    def download_link(self):
        if not self._download_link:
            return "Ожидает генерации после оплаты"
        return self._download_link

    def process(self, quantity: int = 1):
        if not self._download_link:
            self.generate_download_link()
        print(f"На email клиента отправлено {quantity} ключей для '{self.name}'. Ссылка: {self._download_link}")

    def calculate(self) -> float:
        format_multipliers = {
            'pdf': 1.0, 'epub': 1.1, 'mobi': 1.15,
            'mp3': 0.9, 'flac': 1.5, 'mp4': 1.2,
            'mkv': 1.3, 'psd': 1.8, 'ai': 2.0,
            'stl': 1.6, 'zip': 0.8
        }
        multiplier = format_multipliers.get(self._file_format.lower(), 1.0)
        return round(self.price * multiplier, 2)
    
    def generate_download_link(self) -> str:
        self._download_link = f"https://download.example.com/{self.product_id}.{self._file_format.lower()}"
        return self._download_link
    
    def __str__(self) -> str:
        return f"{super().__str__()}[Формат: {self._file_format}] (Ссылка: {self.download_link})"