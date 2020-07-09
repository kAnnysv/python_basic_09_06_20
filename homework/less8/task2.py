class NotZeroError(Exception):
    pass


class Division:

    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider
        self.valid()

    def valid(self):
        if self.divider == 0:
            raise NotZeroError

    def __str__(self):
        return f'{self.divider} / {self.dividend} = {self.divider / self.dividend}'


if __name__ == '__main__':

    try:
        num_1 = Division(4, 5)
        num_2 = Division(3, 0)

        print(num_1)
        print(num_2)

    except NotZeroError:
        print(f'на 0 делить нельзя')
