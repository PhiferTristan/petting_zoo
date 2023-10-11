from .animal import Animal
from movements import Slithering

class Sunbeam(Animal, Slithering):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.slithering = True
        self.slither_speed = 4
    