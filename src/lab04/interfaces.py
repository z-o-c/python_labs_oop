from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        """Возвращает строковое представление объекта"""
        pass

class Comparable(ABC):
    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнивает текущий объект с другим
        Обычно возвращает
         1  (если текущий больше)
        -1  (если текущий меньше)
         0  (если равны)
        """
        pass