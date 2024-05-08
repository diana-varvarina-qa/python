import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '700d27dc87f00414282732183c3c9aba'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '2221'
TRAINER_NAME = 'Boing'
def test_status_code(): 
    response = requests.get(url = f'{URL}/pokemons',params = {'trainer_id' :TRAINER_ID})
    assert response.status_code == 200

def  test_part_of_response(): 
    response_get = requests.get(url = f'{URL}/pokemons',params = {'trainer_id' :TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'Boing'


@pytest.mark.parametrize('key, value', [('name','Бульбазавр'),('trainer_id', TRAINER_ID), ('id', '26425')])   
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value