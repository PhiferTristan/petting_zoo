# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Goat:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Sheep:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Alpaca:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Horse:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Python:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Boa:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Viper:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Sunbeam:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Splitjaw:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Turtle:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Newt:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Koi:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Catfish:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Toad:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True



miss_fuzz = Llama("Miss Fuzz", "domestic llama")

peaches = Goat("Peaches", "domestic goat")

patches = Sheep("Goat", "domestic sheep")

alfonz = Alpaca("Alfonz", "domestic alpaca")

kaptain = Horse("Kaptain", "Mustang")

pybert = Python("Pybert", "Ball Python")

bob = Boa("Bob", "Long Tail Boa")

val = Viper("Val", "Cottonmouth")

shorty = Sunbeam("Shorty", "Shining sunbeam")

viktor = Splitjaw("Viktor", "smooth-scaled splitjaw")

john = Turtle("John", "Painted turtle")

neal = Newt("Neal", "Eastern newt")

kyle = Koi("Kyle", "Bekko")

kat = Catfish("Kat", "Blue catfish")

jiraya = Toad("Jiraya", "scroll toad")


print(miss_fuzz.date_added)
print(jiraya.name)
