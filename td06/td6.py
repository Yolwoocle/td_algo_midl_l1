import random
import tqdm

def est_trie(tab, f=None):
    if f == None:
        f = len(tab)
    for i in range(1, f):
        if tab[i] < tab[i-1]:
            return False
    return True

def permuter(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]

def tri_tableau(tab):
    n = len(tab)
    assert True, "Pre-cond"
    ...
    assert est_trie(tab, n), "Post-cond"
    return

def tri_selection(tab):
    n = len(tab)
    assert True, "Pre cond"
    
    i = 0
    while i < n-1:
        m = i
        for j in range(i+1, n):
            if tab[j] < tab[m]:
                m = j
        permuter(tab, i, m)
        i += 1
        assert est_trie(tab, i), "Invariant"
    assert est_trie(tab, n), "Post cond"
    return tab

def tri_insertion(tab):
    n = len(tab)
    assert True, "pre cond"
    i = 0
    assert est_trie(tab, i), "invariant"
    while i < n:
        j = i
        while tab[j] < tab[j-1] and 0 < j:
            permuter(tab, j, j-1)
            j -= 1
        i += 1
        assert est_trie(tab, i), "invariant"
    assert est_trie(tab, n), f"post cond : {tab}"
    return tab


def vide():
    return None
def liste(t, q):
    return t, q
def tete(li):
    return li[0]
def queue(li):
    return li[1]
def est_vide(li):
    return li == None

def est_inf_eg(li, n):
    li_act = li
    while not est_vide(li_act):
        if tete(li_act) > n:
            return False
        li_act = queue(li_act)
    return True

def est_sup(li, n):
    li_act = li
    while not est_vide(li_act):
        if tete(li_act) <= n:
            return False
        li_act = queue(li_act)
    return True

def li_alea(a, b, len_max, len_min=0):
    def aux(long):
        if long == 0:
            return vide()
        return liste(random.randint(a, b), aux(long - 1))
    return aux(random.randint(len_min, len_max))


def partitionner_pivot_it(li, pivot):
    inf = vide()
    sup = vide()
    li_act = li
    while not est_vide(li_act):
        if tete(li_act) <= pivot:
            inf = liste(tete(li_act), inf)
        else:
            sup = liste(tete(li_act), sup)
        li_act = queue(li_act)
    return inf, sup

def partitionner_pivot(li, pivot):
    if est_vide(li):
        return li, li
    
    inf, sup = partitionner_pivot(queue(li), pivot)
    t = tete(li)
    if t <= pivot:
        return liste(t, inf), sup
    else:
        return inf, liste(t, sup)

def concatener_listes(li1, li2):
    if est_vide(li1):
        return li2
    return liste(tete(li1), concatener_listes(queue(li1), li2))

def tri_rapide(li):
    if est_vide(li) or est_vide(queue(li)):
        return li
    
    piv = tete(li)
    inf, sup = partitionner_pivot(queue(li), piv)
    inf_tri = tri_rapide(inf)
    sup_tri = tri_rapide(sup)
    concatener_listes(inf_tri, liste(piv, sup_tri))
    
def est_trie_chain(li):
    if est_vide(li) or est_vide(queue(li)):
        return True
    if tete(li) > tete(queue(li)):
        return False
    return est_trie_chain(queue(li))

def extraire_min(li):
    assert not est_vide(li), "pre cond"
    if est_vide(queue(li)):
        return tete(li), vide()

    m, nqueue = extraire_min(queue(li))
    if m < tete(li):
        return m, liste(tete(li), nqueue)
    else:
        return tete(li), queue(li)

def est_elt_inf(li, x):
    if est_vide(li):
        return True
    if x > tete(li):
        return False
    return est_elt_inf(queue(li), x)

def compter(li, x):
    if est_vide(li):
        return 0
    if tete(li) == x:
        return 1 + compter(queue(li))
    return compter(queue(li))

def tri_selection_rec(li):
    if est_vide(li):
        return li
    
    m = extraire_min()
    
################################################################################

def test_tri(fonc, nom):
    print(f"Test tri {nom}...")    
    for i in tqdm.trange(1000):
        tab = [random.randint(0, 40) for i in range(random.randint(0, 20))]
        trie = fonc(tab[:])
        assert trie == sorted(tab[:]), f"Test {i} :\n\tDonné {tab[:]}\n\tReçu {trie}"
    print("  OK") 
    
def test_partitionner():
    print("Test partitionner...")
    for i in tqdm.tqdm(range(1000)):
        tab = li_alea(0, 30, 10)
        piv = random.randint(0, 40)
        inf, sup = partitionner_pivot(tab, piv)
        assert est_inf_eg(inf, piv) and est_sup(sup, piv), f"Test {i} :\n\tDonné {tab[:]}, {piv}\n\tReçu {inf}, {sup}"
    print("  OK")   

def test_concatener_listes(): 
    print("Test concatener_listes...")
    for i in tqdm.tqdm(range(1000)):
        tab1 = li_alea(0, 30, 5)
        tab2 = li_alea(0, 30, 5)
        tab = concatener_listes(tab1, tab2)
        def verif2(tab2_ref, tab):
            if est_vide(tab2_ref):
                return True
            if tete(tab2_ref) != tete(tab):
                return False
            return verif2(queue(tab2_ref), queue(tab))
        def verif1(tab1_ref, tab):
            if est_vide(tab1_ref):
                return verif2(tab2, tab)
            if tete(tab1_ref) != tete(tab):
                return False
            return verif2(queue(tab1_ref), queue(tab))
        
        assert verif1(tab1, tab), f"Test {i} :\n\tDonné {tab1}, {tab2}\n\tReçu {tab}"
    print("  OK")

def test_est_trie():
    print(est_trie( (1, None) ), "t")
    print(est_trie( (None) ), "t")
    print(est_trie( (1, (2, (5, None))) ), "t")
    print(est_trie( (1, (3, (2, None))) ), "f")
    print(est_trie( (10, (3, (2, None))) ), "f")
    print(est_trie( (1, (2, (3, (4, (3, None))))) ), "f")
    print(est_trie( (1, (2, (3, (4, None)))) ), "t")


def test_tri_rapide():
    print(f"Test tri rapide...")    
    for i in tqdm.trange(1000):
        tab = li_alea(0, 30, 10)
        trie = tri_rapide(tab)
        assert est_trie_chain(trie), f"Test {i} :\n\tDonné {tab[:]}\n\tReçu {trie}"
    print("  OK") 

def test_extraire_minimum():
    print(f"Test extraire minimum...")    
    for i in tqdm.trange(1000):
        tab = li_alea(0, 30, 10, 1)
        m, ntab = extraire_min(tab)
        print(tab, "\t", m, "\t", ntab, "\n")
        assert est_elt_inf(tab, m), f"Test {i} :\n\tDonné {tab[:]}\n\tReçu {m}"
    print("  OK") 
    

def main():
    test_tri(tri_selection, "selection")
    test_tri(tri_insertion, "insertion")
    test_partitionner()
    test_concatener_listes()
    test_tri_rapide()
    test_extraire_minimum()
main()