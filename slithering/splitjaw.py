from datetime import date

class Splitjaw:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()