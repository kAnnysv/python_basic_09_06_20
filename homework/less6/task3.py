class Worker:
    def __init__(self, name, surname, position,
                 wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position,
                 wage, bonus):
        super().__init__(name, surname, position,
                         wage, bonus)

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))


worker1 = Position('Chak', 'Ivanov', 'Menager', 10000, 2000)

worker1.get_full_name()
worker1.get_total_income()

