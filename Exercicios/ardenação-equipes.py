equipes = [('Equipe A', 85), ('Equipe B', 90), ('Equipe C', 53), ('Equipe D', 90), ('Equipe E', 99)]

def ordena(a):
    for iter in range(len(a) - 1, 0, -1):
        for i in range(len(a) - 1):
            # Compare pelo segundo elemento (a pontuação)
            if a[i][1] > a[i + 1][1]:
                aux = a[i]
                a[i] = a[i + 1]
                a[i + 1] = aux
    return a  # Retorna a lista ordenada

x = ordena(equipes)
print(x)
