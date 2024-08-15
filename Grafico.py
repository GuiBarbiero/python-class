import matplotlib.pyplot as plt
x = [i for i in range(-15,16)]
y = [i ** 2 for i in x]

plt.plot(x ,y, marker='o', linestyle='-')
plt.title('Grafico de coordenadas')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)

plt.show()