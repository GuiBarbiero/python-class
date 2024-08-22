'''
c = int(input("Diga o tanto de colunas")) # com esse valor eu já determino o tanto de colunas
l = int(input("Diga o tanto de linhas"))  # com esse valor eu já determino o tanto de 

matriz = []
for j in range(l): # percorre até o valor de l
    linha = [] # vai armazenar os valores
    for i in range(c): # percorre o tanto de colunas que vai ter
        linha.append(int(input(":"))) # adiciona na lista os valores que vamos colocar
    print(linha)
    matriz.append(linha)
    print(matriz)
'''
# Criar uma matriz com todos elementos iguais a zero (o usuario vai dizer a quantidade de linhas e colunas)
L = int(input("Digite a quantidade de linhas da matriz: "))
C = 10

matriz = []

for i in range(L):
    linha = [0] * C
    matriz.append(linha)

print("\nMatriz resultante:")
for linha in matriz:
    print(linha)