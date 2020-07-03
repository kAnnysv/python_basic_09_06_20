class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начал движение'

    def stop(self):
        return f'{self.name} остановился'

    def turn(self, direction):
        return f'{self.name} повернул на {direction}'

    def show_speed(self):
        return f'{self.name} движется со скоростью {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed}')
        if self.speed > 60:
            return f'У {self.name} Привышение скорости'


class Sport_car(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class Work_car(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed}')
        if self.speed > 40:
            return f'У {self.name} Привышение скорости'



class Police_car(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



Ford = TownCar(70, 'Синий', 'Ford', False)
Ferrari = Sport_car(200, 'Красный', 'Ferrari', True)
Hino = Work_car(50, 'Зеленый', 'Hino', False)
UAZ = Police_car(80, 'Белый', 'UAZ', True)

print(Ford.go(), Ford.turn('Лево'))
print(Ford.show_speed())
print(Ferrari.go(), Ferrari.show_speed(), Ferrari.turn('право'))
print(Ferrari.stop())
print(Hino.go())
print(Hino.show_speed())
print(UAZ.is_police)
