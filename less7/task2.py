from abc import ABC, abstractmethod


class Clothes(ABC):
    unit = 'dm**2'

    def __init__(self):
        self.fabric_area = None

    @property
    def area(self):
        if self.fabric_area is None:
            self.calc_fabric_area()
        return self.fabric_area

    @abstractmethod
    def calc_fabric_area(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}: {self.area:.2f} {self.unit}'


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self._v = v

    def calc_fabric_area(self):
        self.fabric_area = self._v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        super().__init__()
        self._h = h

    @property
    def size(self):
        return self._h

    def calc_fabric_area(self):
        self.fabric_area = 2 * self._h + 0.3


class ClothesCollection:
    def __init__(self):
        self._collection = []

    def apnd(self, itm):
        if isinstance(itm, Clothes):
            self._collection.append(itm)

    def total_fabric_area(self):
        return sum(el.area for el in self._collection)

    def __str__(self):
        return f'Общая площадь ткани -{self.total_fabric_area()} dm**2 '


costume1 = Costume(6)
coat1 = Coat(54)
coat2 = Coat(64)
print(coat2)
collection1 = ClothesCollection





