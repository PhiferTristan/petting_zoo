from animals import Animal
from datetime import date

class Llama(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def feed_llama(self):
        return f'{self.name} was fed {self.food} after being sung to on {date.today().strftime("%m/%d/%Y")}'
        