import requests

api_key = 'd4cfc9c1-2d52-46e7-be73-5fd8f9635104'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
