import math

def somme_lignes(matrice):
    li = [0] * len(matrice)
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            li[i] += matrice[i][j]
    return li

def somme_colonnes(matrice):
    li = [0] * len(matrice[0])
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            li[j] += matrice[i][j]
    return li

mat = [
    [1, 2, 3],
    [5, 6, 7], 
    [9, 10, 11]
]
print(somme_lignes(mat))
print(somme_colonnes(mat))