# lembre-se de instalar a biblioteca Requests
'''
import requests

url = 'https://viacep.com.br/ws/01001000/json/'

r = requests.get(url)
print(f'Resposta: {r}')
print(r.text)

# faça um programa em que o usuário digitará o CEP de entrega do local


import requests
cep = input("Diga o seu cep [Sem traço]")
url = f'https://viacep.com.br/ws/{cep}/json/'

r = requests.get(url)
print(f'Resposta: {r}')
print(r.text)

'''

import requests
def poke(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    r = requests.get(url)
    #print(r.json()) # ISSO PRINTA O JSON INTEIROdicionario
    r = r.json()
    id = r['id']
    tipo = r['types'][0]['type']['name']
    return [id, tipo]

pokemon = input("Diga o nome do pokemon desejado")
var = poke(pokemon)

print(f"o id do {pokemon} é {var[0]}.")
print(f'{pokemon} é do tipo {var[1]}') # printa o tipo do pokemon no caso elétrico



