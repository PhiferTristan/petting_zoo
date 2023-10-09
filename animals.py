# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

class Goat:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

class Sheep:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

class Alpaca:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

class Horse:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True

class Python:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.slithering = True
        self.date_added = date.today()

class Boa:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.slithering = True
        self.date_added = date.today()

class Viper:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.slithering = True
        self.date_added = date.today()

class Sunbeam:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.slithering = True
        self.date_added = date.today()

class Splitjaw:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.slithering = True
        self.date_added = date.today()

class Turtle:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True

class Newt:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True

class Koi:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True

class Catfish:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True

class Toad:
    def __init__(self) -> None:
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True



miss_fuzz = Llama()
miss_fuzz.name = "Miss Fuzz"
miss_fuzz.species = "domestic llama"
peaches = Goat()
peaches.name = "Peaches"
peaches.species = "domestic goat"
patches = Sheep()
patches.name = "Goat"
patches.species = "domestic sheep"
alfonz = Alpaca()
alfonz.name = "Alfonz"
alfonz.species = "domestic alpaca"
kaptain = Horse()
kaptain.name = "Kaptain"
kaptain.species = "Mustang"
pybert = Python()
pybert.name = "Pybert"
pybert.species = "Ball Python"
bob = Boa()
bob.name = "Bob"
bob.species = "Long Tail Boa"
val = Viper()
val.name = "Val"
val.species = "Cottonmouth"
shorty = Sunbeam()
shorty.name = "Shorty"
shorty.species = "Shining sunbeam"
viktor = Splitjaw()
viktor.name = "Viktor"
viktor.species = "smooth-scaled splitjaw"
john = Turtle()
john.name = "John"
john.species = "Painted turtle"
neal = Newt()
neal.name = "Neal"
neal.species = "Eastern newt"
kyle = Koi()
kyle.name = "Kyle"
kyle.species = "Bekko"
kat = Catfish()
kat.name = "Kat"
kat.species = "Blue catfish"
jiraya = Toad()
jiraya.name = "Jiraya"
jiraya.species = "scroll toad"

print(miss_fuzz.date_added)
print(jiraya.name)
