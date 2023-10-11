from datetime import date
from .animal import Animal
from movements import Slithering

class Viper(Animal, Slithering):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.slithering = True
        self.slither_speed = 6

    def feed(self):
        return f'{self.name} was fed {self.food} after giving her time to control her mouth on {date.today().strftime("%m/%d/%Y")}'
    