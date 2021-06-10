#1a
pokemon_list = ["Pikachu", "Eevee", "Ditto"]

print(pokemon_list)

pokemon_list.append("Landorus")

print(pokemon_list)

#pokemon_list.remove("Eevee")
#print(pokemon_list)

#pokemon_list.pop(0)
#print(pokemon_list)

print(pokemon_list[3])

#1b

my_team = ["Landorus", "Weedle", "Spearow", "Pidgey", "Gardevoir"]
print(my_team)

#1c

pokedex = pokemon_list + my_team

print(pokedex)

#1d

pokedex.insert(3, "Rattata")

print("Random text")
print(pokedex)

#1e
print(len(pokedex))

#1f

for item in pokedex:
    print(item)

#1g

if 'Charizard ' in pokedex:
    print(f'Charizard is in the pokedex list')
else:
    print("You don't have it!")
    