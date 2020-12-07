def mea(c, n):
    b = c//n
    r = c-b*n
    return r

p = 2**(89)-1

print(mea(p,4))
print(mea(p,5))