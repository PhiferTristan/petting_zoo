from . import Attraction
from movements import Walking


class PettingZoo(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f"{animal} doesn't like to be pet, so please don't put in the {self.attraction_name}")

    def add_animal_type_check(self, animal):
        if isinstance(animal, Walking):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            print(f"{animal} doesn\'t belong in {self.attraction_name}")
