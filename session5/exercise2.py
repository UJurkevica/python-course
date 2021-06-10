import collections


my_pokemon2 = {
    "pokemon" : "Charizard",
    "type" : "fire",
    "level" : 55,
}
print(my_pokemon2)
# = sign needed to be replaced with :

#2a

my_status = {
    "name" : "Patricia",
    "age" : 25,
    "occupation" : "Technician",
}

print(my_status)

my_status['Hobbies'] = "reading", "painting"

print(my_status)

del my_status['age']
print(my_status)

my_status['name'] = "Ana"

print(my_status)

print(my_status['Hobbies'][1])
print(my_status['Hobbies'])

#2b

my_pokemon = {
    "pokemon" : "Rapidash",
    "type" : "Fire",
    "level" : 30
}
print(my_pokemon)

#2c
my_pokemon['move'] = "Flame Wheel"

print(my_pokemon)

#2d

for value in my_pokemon.values():
    print(value)

for key in my_pokemon.keys():
    print(key)


my_pokemon['move'] = "Flame Wheel", "Agility"

print(my_pokemon)

for value in my_pokemon['move']:
    print(value)
