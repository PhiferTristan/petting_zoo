from .animal import Animal
from movements import Swimming, Walking


class Goose(Animal, Swimming, Walking):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.swim_speed = 4
        self.walk_speed = 3
