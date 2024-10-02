a = [12,43,65,31,34,6,51]

print(a)
for iteracao in range (len(a)-1,0,-1):
    print(iteracao)    
    for i in range(iteracao):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
        print(a)