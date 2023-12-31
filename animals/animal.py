from datetime import date

class Animal:
    def __init__(self, name, species, food, chip_num) -> None:
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_num
        self.date_added = date.today()

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, num):
        pass
    
    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self) -> str:
        return f"{self.name} is a {self.species}."