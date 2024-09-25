def calculadora(lista_compras, supermercado):
    total = 0
    for item in lista_compras:
        if item in supermercado:
            total += supermercado[item]
        else:
            print(f"Não temos o produto: {item}")
    return total

lista_de_compras = 'biscoito','chocolate','farinha'
supermercado = {
    'amaciante':4.99,
    'arroz': 10.90,
    'biscoito':1.69,
    'cafe': 6.98,
    'chocolate': 3.79,
    'farinha': 2.99
}

total = calculadora(lista_de_compras, supermercado)
print(f'O valortotal dos itens disponiceis na loja é:{total}')

