class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width


class Asphalt(Road):
    def __init__(self, length, width, mass, thickness):
        super().__init__(length, width)
        self.mass = mass
        self.thickness = thickness

    def asph_mass(self):
        return self._length * self._width * self.mass * self.thickness


asph_mass_road = Asphalt(20, 5000, 25, 5)
print(f'{(asph_mass_road.asph_mass()) / 1000} т')
