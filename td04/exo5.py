def prod_elts(li):
    if li == None:
        return 1
    else:
        return li[0] * prod_elts(li[1])
    
li = (1, (3, (5, None)))
print(prod_elts(li))