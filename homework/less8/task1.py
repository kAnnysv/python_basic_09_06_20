class Invalid_date(Exception):
    pass


class Data:
    def __init__(self, input_date):
        self.data = input_date

    @classmethod
    def extract(cls, input_date):
        date_lict = list(map(int, input_date.split('-')))
        cls.is_valid(date_lict)
        return cls(date_lict)

    @staticmethod
    def is_valid(input_date):
        if len(input_date) == 3 and 32 > input_date[0] > 0 and 13 > input_date > 0 and input_date > 0:
            return input_date
        else:
            raise Invalid_date(f'Не верно введена дата')


try:
    Data.extract('12-11-2020')
except Invalid_date as e:
    print(e)
"""Вроде всё правильно, но неработает"""