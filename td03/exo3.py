def est_croissant(tab: list) -> bool:
    for i in range(len(tab) - 1):
        if tab[i] > tab[i+1]:
            return False
    return True

assert est_croissant([0, 1, 2, 2])
assert est_croissant([2, 1]) == False
assert est_croissant([1]) 
assert est_croissant([]) 
assert est_croissant([0, 1, 2, 1]) == False 
assert est_croissant([1, 2, 2, 1]) == False 
assert est_croissant([0, 1, 1, 1, 1, 0]) == False 
assert est_croissant([0, 1, 1, 1, 1]) == True 
assert est_croissant([0, 0, 0, 100]) == True 

def dernier_negatif(tab: list[int]):
    assert len(tab) > 0 
    assert est_croissant(tab) 
    assert tab[0] < 0 
    assert tab[len(tab)-1] > 0
    def invariant():
        return 0 <= i < len(tab)-1 and tab[i] <= 0
    
    i = 0
    assert invariant()
    while tab[i+1] <= 0:
        i += 1
        assert invariant()
    assert 0 <= i < len(tab)-1 and tab[i] <= 0 and tab[i+1] > 0 
    return i
    
    
assert dernier_negatif([-2, -2, -1, 0, 1, 2, 3, 4]) == 3
assert dernier_negatif([-1, 1]) == 0
assert dernier_negatif([-1, 1, 2]) == 0
assert dernier_negatif([-1, -1, 1, 2]) == 1
assert dernier_negatif([-1, 0, 0, 0, 0, 100]) == 4

def dernier_negatif_dichotomie(tab: list[int]):
    assert len(tab) > 0 
    assert est_croissant(tab) 
    assert tab[0] < 0 
    assert tab[len(tab)-1] > 0
    def invariant():
        return 0<=i<j<len(tab) and tab[i] <= 0 and tab[j]>0
    
    i = 0
    j = len(tab)-1
    
    assert invariant()
    while i+1 < j:
        m = (i+j)//2
        if tab[m] > 0:
            j = m
        else:
            i = m
        assert invariant()
    assert invariant() and i+1 >= j 
    return i


    
assert dernier_negatif_dichotomie([-2, -2, -1, 0, 1, 2, 3, 4]) == 3
assert dernier_negatif_dichotomie([-1, 1]) == 0
assert dernier_negatif_dichotomie([-1, 1, 2]) == 0
assert dernier_negatif_dichotomie([-1, -1, 1, 2]) == 1
assert dernier_negatif_dichotomie([-1, 0, 0, 0, 0, 100]) == 4