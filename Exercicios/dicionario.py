

# 1
frutaria = {
    'Melancia' :'Verde',
    'Uva' :'Roxa',
    'Kiwi' :'rosa',
}
print(frutaria)
#2
print(frutaria['Melancia'])

# 3
frutaria['Kiwi'] = 'Verde'
print(frutaria)

# 4
frutaria['Melancia'] = 'Vermelha'
print(frutaria)

# 5
frutaria.pop('Melancia')
print(frutaria)

# 06
for i in frutaria.keys():
    print(i)

# 7
for i in frutaria.values():
    print(i)

# 08

res = 'Banana' in frutaria
print(res)

# 09

frutariaB = {
    'Pessego':'Amarelo',
    'Tomate': 'Laranja'
}

#10
print(len(frutariaB))
