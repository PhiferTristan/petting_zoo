from animals import Animal

class Sunbeam(Animal):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.slithering = True
    