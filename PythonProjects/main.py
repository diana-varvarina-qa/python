import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '700d27dc87f00414282732183c3c9aba'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "di.varvarina@yandex.ru",
    "password": "Iloveqa1"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
     "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_update = {
    "pokemon_id": "26417",
    "name": "Краш",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
body_pokebol = {
    "pokemon_id": "26417"
}
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''


'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print(response_update.text)

response_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokebol)
print(response_pokebol.text)






