a = [
    [1,2,8],
    [5,7,9]
]
#print(a[0]) # printa minha primeira lista no caso [1,2,8]
#print(a[0][0]) # printa meu primeiro item da primeira lista.
def printa(a):
    for i in a:
        for j in i:
           print(j, end=" ")
        print()

a = [
    [1,2,8],
    [5,7,9]
]

printa(a)