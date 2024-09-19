informações = {
    "alice": [20,'f']

}


quantidade = int(input("Diga quantos valores voce deseja adicionar"))

for i in range(quantidade):
    nomes = input("Diga os nomes que você deseja adicionar")
    idade = input("Diga a idade da pessoa")
    sexo = input("Diga o sexo da pessoa")
    informações[nomes] = [idade,sexo]

print(informações)

# pegar a idade de alguem pelo dicionario

print(informações['AA'][0]) # assim dentro da lista do AA eu pego a idade dela
#por ser o primeiro elemento da losta
