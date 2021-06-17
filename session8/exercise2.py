import requests
from pprint import pprint as p


response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
pokemons_status = response.json()
p(pokemons_status)


pokemons_status.keys()

#pokemons_status['weight']
#https://any-api.com/

