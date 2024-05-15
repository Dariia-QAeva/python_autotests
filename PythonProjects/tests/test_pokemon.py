import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'bf0beae92e7b2c6665b823c4d1971d81'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '2607'
    
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer id': TRAINER_ID})
    assert response.status_code == 200
def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TRAINER_ID}, timeout=5)
    assert response.json()['data'][0]['trainer_name'] == 'Трололо'
    
    
