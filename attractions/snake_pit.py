class SnakePit:

    def __init__(self, name) -> None:
        self.attraction_name = name
        self.description = "slimy, slithering critters to be scared of"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        return f'{self.animals[-1]}'
        