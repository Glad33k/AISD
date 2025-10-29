def babelkowe(lista, n):
    for i in range(n):
        for j in range(n - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def wybieranie(lista, n):
    for i in range(n):
        indexik = i
        for j in range(i + 1, n):
            if lista[j] < lista[indexik]:
                indexik = j
        lista[i], lista[indexik] = lista[indexik], lista[i]
        print(lista)
    return lista

def wstawianie(lista,n):
    for i in range(1, n):
        pom = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > pom:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = pom
        print(lista)

    return lista



#print(babelkowe([3, 4, 0, 7, 1, 5, 2, 8, 9, 6], 10))
#print(wybieranie([3, 4, 0, 7, 1, 5, 2, 8, 9, 6], 10))
print(wstawianie([3, 4, 0, 7, 1, 5, 2, 8, 9, 6], 10))
