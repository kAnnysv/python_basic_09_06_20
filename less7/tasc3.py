class Cell:
    def __init__(self, number):
        try:
            self.number = int(number)
        except Exception as e:
            print(f'Не целое число {e}')

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            return f'Не выполнимая операция'

    def __mul__(self, other):
        return Cell(self.number * self.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def __str__(self):
        return f'{self.number * "*"} - {self.number}'

    def make_order(self, line_cells):
        line = f'{"*" * line_cells}\n' * (self.number // line_cells)
        line += f'{"*" * (self.number % line_cells)}'
        return line


cell1 = Cell(16)
cell2 = Cell(10)
cell3 = Cell(3)
print(cell1 + cell2 + cell3)
print(cell2 - cell1)
print(cell2 - cell3)
print(cell1 / cell3)
print(cell1 * cell2) #Почему не корректно работает умножение ? 16*10 выдает 256
print(cell3 * cell2)# 3* 10 = 9
print(cell1.make_order(5))
print(cell2.make_order(3))