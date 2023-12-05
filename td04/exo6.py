def der_elt(li):
    if li == None:
        raise Exception("non")
    elif li[1] == None:
        return li[0]
    else:
        return der_elt(li[1])
    
li = (0, (1, (2, (3, (4, (5, None))))))
print(der_elt(li))