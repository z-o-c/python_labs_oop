from src.lab03.model import Product
from src.lab04.interfaces import Printable, Comparable
from datetime import date, timedelta
from src.lab01.validate import validate_stock


class FoodProduct(Product, Printable, Comparable):
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

    @property
    def is_expired(self) -> bool:
        expiration_date = self._production_date + timedelta(days=self._shelf_life_days)
        return date.today() > expiration_date

    def to_string(self) -> str:
        status = "Просрочен" if self.is_expired else "Срок годности в норме"
        return f"[ЕДА] {self.name} | Остаток: {self.stock} | Статус: {status}"

    def compare_to(self, other) -> int:
        self_exp = self.production_date + timedelta(days=self.shelf_life_days)
        other_exp = other.production_date + timedelta(days=other.shelf_life_days)
        if self_exp > other_exp:
            return 1
        if self_exp < other_exp:
            return -1
        return 0

    def process(self, quantity: int = 1):
        if self.stock < quantity:
            raise ValueError(f"Недостаточно товара '{self.name}'. В наличии: {self.stock}")
        self.stock -= quantity
        print(f"[СКЛАД] Отгружено {quantity} шт. товара '{self.name}'. Остаток: {self.stock}")

    def calculate(self) -> float:
        if self._stock <= 0:
            raise ValueError(f"Товар {self.name} закончился на складе")

        if self.is_expired:
            self.deactivate()
            raise ValueError(f"Товар {self.name} просрочен. Он автоматически снят с продажи.")

        expiration_date = self._production_date + timedelta(days=self._shelf_life_days)
        days_left = (expiration_date - date.today()).days

        if days_left <= 3:
            return round(self.price * 0.5, 2)

        return round(self.price, 2)

    def __str__(self) -> str:
        return f"{super().__str__()} (Дата изготовления: {self._production_date}. Срок годности: {self._shelf_life_days} дн.)"


class DigitalProduct(Product, Printable, Comparable):
    def __init__(self, name, price, discount, category, product_id, file_format: str, file_size: int):
        super().__init__(name, price, discount, category, product_id)

        self._file_format = file_format
        self._download_link = ""
        self._file_size = file_size

    @property
    def file_format(self):
        return self._file_format

    @property
    def download_link(self):
        if not self._download_link:
            return "Ожидает генерации после оплаты"
        return self._download_link

    @property
    def file_size(self):
        return self._file_size

    def to_string(self) -> str:
        return f"[ЦИФРОВОЙ] {self.name} | Формат: {self.file_format} | Размер: {self.file_size} МБ | Ссылка: {self.download_link}"

    def compare_to(self, other) -> int:
        if self.file_size > other.file_size:
            return 1
        if self.file_size < other.file_size:
            return -1
        return 0

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
        return f"{super().__str__()} [Формат: {self.file_format}] (Ссылка: {self.download_link})"
