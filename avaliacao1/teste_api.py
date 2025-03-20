'''
    Criado apenas para verificar o que era retornado na requisição.
'''

import requests

response = requests.get('https://anapioficeandfire.com/api/characters/20').json()
print(response)