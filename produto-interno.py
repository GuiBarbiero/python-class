def prodint(v, w):
    if len(v) != len(w):
        return None

    soma = 0
    for i in range(len(v)):
        soma +=  v[i] * w[i]
    return soma


resultado =  prodint([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9])
print(resultado)

# CUIDADO COM IDENTAÇÃO