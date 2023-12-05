def appartient(x, li):
    if li == None:
        return False
    elif x == li[0]:
        return True
    else:
        return appartient(x, li[1])


li = (0, (1, (2, (3, (4, (5, None))))))
print(appartient(4, li))
print(appartient(7, li))
print(appartient(0, li))
print(appartient(-1, li))