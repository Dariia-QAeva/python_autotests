import requests
URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'bf0beae92e7b2c6665b823c4d1971d81'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
body_pokemons = {
    "name": "Cvbhyj",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_pokebol = {
    "pokemon_id": "18557"
}
body_name = {
    "pokemon_id": "18557",
    "name": "NoName",
    "photo": "https://dolnikov.ru/pokemons/albums/022.png"
}
responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(responce_create.text)

responce_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER, json = body_pokebol)
print(responce_pokeboll.text)

responce_name = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_name)
print(responce_name.text)