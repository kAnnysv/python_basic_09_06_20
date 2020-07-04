from time import sleep


class Trafficlight:
    __color = ['красный', 'жёлтый', 'зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор зажёг {Trafficlight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(10)
            i += 1


traficLight = Trafficlight()
traficLight.running()
