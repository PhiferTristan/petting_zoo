from .animal import Animal
from movements import Swimming

class Koi(Animal, Swimming):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.swimming = True
        self.swim_speed = 5
    