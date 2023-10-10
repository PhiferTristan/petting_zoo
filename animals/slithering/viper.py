from animals import Animal
from datetime import date

class Viper(Animal):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        return f'{self.name} was fed {self.food} after giving her time to control her mouth on {date.today().strftime("%m/%d/%Y")}'
    