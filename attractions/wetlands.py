class Wetlands:
    def __init__(self, name) -> None:
        self.attraction_name = name
        self.description = "all the cuties that like the water"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return f"{self.animals[-1]}"
