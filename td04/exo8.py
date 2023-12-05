def lire_elt(li, i):
    if li == None or i < 0:
        raise Exception("out of bounds lol")
    if i == 0:
        return li[0]
    return lire_elt(li[1], i-1)

li = (0, (1, (2, (4, (4, (5, None))))))
print(li)
for i in range(10):
    print(i, lire_elt(li, i))