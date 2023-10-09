from datetime import date

class Sunbeam:
    def __init__(self, name, species, food) -> None:
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self) -> str:
        return f"{self.name} is a {self.species}."
    