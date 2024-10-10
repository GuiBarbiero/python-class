def indice_menor_elemento(lista, posicao_inicial):
    if posicao_inicial < 0 or posicao_inicial >= len(lista):
        return None
    menor_index = posicao_inicial
    for i in range(posicao_inicial, len(lista)):
        if lista[i] < lista[menor_index]:
            menor_index = i
    return menor_index  
lista_exemplo = [5, 3, 8, 1, 4]
indice = indice_menor_elemento(lista_exemplo, 4)
print(indice)
