from datetime import date

from animals.slithering import (Boa, Python, Splitjaw, Sunbeam, Viper)
from animals.swimming import (Catfish, Koi, Newt, Toad, Turtle)
from animals.walking import (Alpaca, Goat, Horse, Llama, Sheep)

from attractions import PettingZoo
from attractions import SnakePit
from attractions import Wetlands


varmint_village = PettingZoo("Varmint Village")
the_slither_inn = SnakePit("The Slither Inn")
critter_cove = Wetlands("Critter Cove")

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow", 100001)
peaches = Goat("Peaches", "domestic goat", "morning", "goat chow", 100002)
patches = Sheep("Patches", "domestic sheep", "midday", "sheep chow", 100003)
alfonz = Alpaca("Alfonz", "domestic alpaca", "midday", "alpaca chow", 100004)
kaptain = Horse("Kaptain", "Mustang", "afternoon", "horse feed", 100005)

varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(peaches)
varmint_village.add_animal(patches)
varmint_village.add_animal(alfonz)
varmint_village.add_animal(kaptain)

pybert = Python("Pybert", "Ball Python", "mice", 100006)
bob = Boa("Bob", "Long Tail Boa", "mice", 100007)
val = Viper("Val", "Cottonmouth", "mice", 100008)
shorty = Sunbeam("Shorty", "Shining sunbeam", "mice", 100009)
viktor = Splitjaw("Viktor", "smooth-scaled splitjaw", "mice", 100010)

the_slither_inn.add_animal(pybert)
the_slither_inn.add_animal(bob)
the_slither_inn.add_animal(val)
the_slither_inn.add_animal(shorty)
the_slither_inn.add_animal(viktor)

john = Turtle("John", "Painted turtle", "turtle chow", 100011)
neal = Newt("Neal", "Eastern newt", "newt chow", 100012)
kyle = Koi("Kyle", "Bekko", "bread crumbs", 100013)
kat = Catfish("Kat", "Blue catfish", "fish feed", 100014)
jiraya = Toad("Jiraya", "scroll toad", "popsicle", 100015)

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

kaptain.chip_number = 555783
print(kaptain.chip_number)
print(critter_cove.last_critter_added)
print(varmint_village.last_critter_added)
print(the_slither_inn.last_critter_added)

print(miss_fuzz.feed_llama())
print(miss_fuzz.feed())
print(kat.feed())
print(val.feed())
