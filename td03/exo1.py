def nom_fonction(params):
    assert "pré-cond"
    ...
    assert "invariant (initialisation)"
    while not "condition d'arrêt":
        ...
        assert "invariant (itération)"
    assert "invariant" and "condition d'arret"
    return "valeur de retour"


def somme(n: int):
    assert n >= 0
    k = 0
    s = 0
    assert s == (k * (k+1)) // 2
    while k < n:
        k += 1
        s += k
        assert s == (k*(k+1)) // 2
    assert s == (k*(k+1)) // 2 and k == n
    return s


print(somme(1))
print(somme(2))
print(somme(3))
print(somme(4))
print(somme(5))
print(somme(6))
print(somme(7))