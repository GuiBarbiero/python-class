def soma (a, b):
    return a + b

l = [1, 2]

resultado = soma(l[0], l[1])  #l[0] assim você coleta os elementos de determinado lugar da lista

resultado = soma(*l)
print(resultado)


# *(nome da lista) eu consigo printar toda a lista de uma vez sem precisar fazer um loop