import matplotlib.pyplot as plt

a = 1
c = 8
l = 8

contador = 0
xadrez = []
for i in range(c):
    linha = []
    for j in range(l):
        if contador == 0:
            linha.append([255,255,255])
            contador = 1
        else:
            linha.append([0,0,0])
            contador = 0
    if contador == 1:
        contador = 0
    else:
        contador = 0
    xadrez.append(linha)

plt.imshow(xadrez)
plt.axis('off')
plt.show()

