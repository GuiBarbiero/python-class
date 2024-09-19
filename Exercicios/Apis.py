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
url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
r = requests.get(url)
#print(r.json()) # ISSO PRINTA O JSON INTEIRO
dicionario = r.json()
print(dicionario['id'])
print(dicionario['name'])
print(dicionario['types'])

