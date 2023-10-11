from .animal import Animal
from movements import Walking

class Sheep(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift
        self.walk_speed = 4
