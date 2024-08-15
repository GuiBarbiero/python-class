# def soma(*param):
#   print(param)
# soma(1,2,3,4)


# =========================

"""def soma(*param):
    soma = 0
    for i in param:
        soma += 
    return soma
    
resultado = soma(1, 2, 3, 5, 6, 7, 8, 9, 10)
print(resultado)
"""
def soma(*numero):
    b = 0
    for i in numero:
        b += i
    return b

qnte = int(input("Digite os valores"))
valores = []
for i in range(qnte):
    valores.append(int(input('Digite o numero:')))
      
print(soma(*valores))

