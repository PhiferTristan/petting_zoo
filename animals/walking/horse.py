from animals import Animal

class Horse(Animal):
    def __init__(self, name, species, shift, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift
        