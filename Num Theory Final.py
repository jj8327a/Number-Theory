#Decrypts Cipher text
def gamal(c, p, g):
    b = c*g//p
    r = c*g-b*p
    return r

#modified euclidean algorithm
def mea(c, n, d, a):
    b = c**a*d//n
    r = c**a*d-b*n
    return r

gamma=2253
a = 65
p = 3167

#finds inverse of gamma^a
def inverse():
    for i in range(0, p):
        global z
        if mea(gamma, p, i, a) == 1:
            z = i
            return i
        else:
            pass


inverse()

cipher = [270, 2224, 1899, 590]
numplain = []
for i in cipher:
    numplain.append(gamal(int(i), p, z))

print(inverse())
print("Numerical Plaintext:", numplain)












