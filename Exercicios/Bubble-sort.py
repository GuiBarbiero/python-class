a = [11,3,4,65,2,23]
print(a)

for tamanho in range(len(a)-1,1,-1):
    for i in range(tamanho):
        if a[i] > a[i + 1]:
           aux = a[i]
           a[i] = a[i+1]
           a[i+1] = aux
        print(a)
    print(tamanho)

