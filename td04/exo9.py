def nb_sup(li):
    def aux(li, som, nb):
        if li == None:
            return (0, som/nb)
        else:
            n_s, moy = aux(li[1], som+li[0], nb+1)
            if li[0] > moy:
                return (n_s+1, moy)
            else:
                return (n_s, moy)
    n_s, moy = aux(li, 0, 0)
    return n_s, moy

li = (0, (1, (2, (4, (4, (5, None))))))
print(li)
print(nb_sup(li))

li = (1, (1, (20, (40, (-1, (5, None))))))
print(li)
print(nb_sup(li))