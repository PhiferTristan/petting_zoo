from slithering import (Boa, Python, Splitjaw, Sunbeam, Viper)
from swimming import (Catfish, Koi, Newt, Toad, Turtle)
from walking import (Alpaca, Goat, Horse, Llama, Sheep)

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning")

peaches = Goat("Peaches", "domestic goat", "morning")

patches = Sheep("Patches", "domestic sheep", "midday")

alfonz = Alpaca("Alfonz", "domestic alpaca", "midday")

kaptain = Horse("Kaptain", "Mustang", "afternoon")

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
print(f'{patches.name} the {patches.species} is available to pet during the {patches.shift} shift.')
