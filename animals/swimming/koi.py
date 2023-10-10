from animals import Animal

class Koi(Animal):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.swimming = True
    