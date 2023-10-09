from slithering import (Boa, Python, Splitjaw, Sunbeam, Viper)
from swimming import (Catfish, Koi, Newt, Toad, Turtle)
from walking import (Alpaca, Goat, Horse, Llama, Sheep)

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")

peaches = Goat("Peaches", "domestic goat", "morning", "goat chow")

patches = Sheep("Patches", "domestic sheep", "midday", "sheep chow")

alfonz = Alpaca("Alfonz", "domestic alpaca", "midday", "alpaca chow")

kaptain = Horse("Kaptain", "Mustang", "afternoon", "horse feed")

pybert = Python("Pybert", "Ball Python", "mice")

bob = Boa("Bob", "Long Tail Boa", "mice")

val = Viper("Val", "Cottonmouth", "mice")

shorty = Sunbeam("Shorty", "Shining sunbeam", "mice")

viktor = Splitjaw("Viktor", "smooth-scaled splitjaw", "mice")

john = Turtle("John", "Painted turtle", "turtle chow")

neal = Newt("Neal", "Eastern newt", "newt chow")

kyle = Koi("Kyle", "Bekko", "bread crumbs")

kat = Catfish("Kat", "Blue catfish", "fish feed")

jiraya = Toad("Jiraya", "scroll toad", "popsicle")


print(miss_fuzz.date_added)
print(jiraya.name)
print(f'{patches.name} the {patches.species} is available to pet during the {patches.shift} shift.')
print(miss_fuzz.feed())
print(val)
print(pybert)
print(kyle)
