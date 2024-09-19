frase = 'Os ratos'
contagem = {

}
for i in frase:
    if i in contagem:
        contagem[i] += 1
    else:
        contagem[i] = 1
print(contagem)
