def app_li_triee(x, li):
    if li == None:
        return False
    elif x < li[0]:
        return False
    elif x == li[0]:
        return True
    else:
        return app_li_triee(x, li[1])

li = (0, (1, (2, (4, (4, (5, None))))))
print(li)
for i in range(9):
    print(i, app_li_triee(i, li))