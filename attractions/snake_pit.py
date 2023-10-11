from . import Attraction
from movements import Slithering

class SnakePit(Attraction):

    def __init__(self, name, description) -> None:
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except ArithmeticError as ex:
            print(f"{animal} doesn\'t belong in {self.attraction_name}")
        