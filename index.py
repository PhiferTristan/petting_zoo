from slithering import (Boa, Python, Splitjaw, Sunbeam, Viper)
from swimming import (Catfish, Koi, Newt, Toad, Turtle)
from walking import (Alpaca, Goat, Horse, Llama, Sheep)

from attractions import PettingZoo
from attractions import SnakePit
from attractions import Wetlands



varmint_village = PettingZoo("Varmint Village")
the_slither_inn = SnakePit("The Slither Inn")
critter_cove = Wetlands("Critter Cove")

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")
peaches = Goat("Peaches", "domestic goat", "morning", "goat chow")
patches = Sheep("Patches", "domestic sheep", "midday", "sheep chow")
alfonz = Alpaca("Alfonz", "domestic alpaca", "midday", "alpaca chow")
kaptain = Horse("Kaptain", "Mustang", "afternoon", "horse feed")

varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(peaches)
varmint_village.add_animal(patches)
varmint_village.add_animal(alfonz)
varmint_village.add_animal(kaptain)

pybert = Python("Pybert", "Ball Python", "mice")
bob = Boa("Bob", "Long Tail Boa", "mice")
val = Viper("Val", "Cottonmouth", "mice")
shorty = Sunbeam("Shorty", "Shining sunbeam", "mice")
viktor = Splitjaw("Viktor", "smooth-scaled splitjaw", "mice")

the_slither_inn.add_animal(pybert)
the_slither_inn.add_animal(bob)
the_slither_inn.add_animal(val)
the_slither_inn.add_animal(shorty)
the_slither_inn.add_animal(viktor)

john = Turtle("John", "Painted turtle", "turtle chow")
neal = Newt("Neal", "Eastern newt", "newt chow")
kyle = Koi("Kyle", "Bekko", "bread crumbs")
kat = Catfish("Kat", "Blue catfish", "fish feed")
jiraya = Toad("Jiraya", "scroll toad", "popsicle")

critter_cove.add_animal(john)
critter_cove.add_animal(neal)
critter_cove.add_animal(kyle)
critter_cove.add_animal(kat)
critter_cove.add_animal(jiraya)

print(f'{patches.name} the {patches.species} is available to pet during the {patches.shift} shift.')

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}.')
for animal in the_slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {the_slither_inn.attraction_name}.')
for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}.')

# for animal in critter_cove.animals:
#     print(f"* {animal.name} the {animal.species}")

attractions = [varmint_village, the_slither_inn, critter_cove]

msg = ""
for attraction in attractions:
    msg += f"{attraction.attraction_name} is where you will find {attraction.description}, like\n"
    for animal in attraction.animals:
        msg += f"* {animal.name} the {animal.species}\n"
    msg += "\n"
print(msg)
# print(critter_cove_list)
