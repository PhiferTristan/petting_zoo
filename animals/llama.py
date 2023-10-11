from datetime import date
from .animal import Animal
from movements import Walking

class Llama(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift
        self.walk_speed = 5

    def feed_llama(self):
        return f'{self.name} was fed {self.food} after being sung to on {date.today().strftime("%m/%d/%Y")}'
        