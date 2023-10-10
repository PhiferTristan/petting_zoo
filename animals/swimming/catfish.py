from animals import Animal
from datetime import date

class Catfish(Animal):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        return f"{self.name} was fed {self.food} after all the other fish are fed on {date.today().strftime('%m/%d/%Y')}"
    