from datetime import date
from .animal import Animal
from movements import Swimming

class Catfish(Animal, Swimming):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.swimming = True
        self.swim_speed = 7

    def feed(self):
        return f"{self.name} was fed {self.food} after all the other fish are fed on {date.today().strftime('%m/%d/%Y')}"
    