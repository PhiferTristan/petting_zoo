from datetime import date

class Turtle:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True