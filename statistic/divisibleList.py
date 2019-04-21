import numpy as np

def divisibleList(a):
    s = 0
    vec = np.zeros(a)
    for i in range(1,a):
        kalan = a%i 
        if kalan == 0: 
            s = s +1
            vec[s] = i
        if kalan ==i:
            s = s+1
            vec[s]= i

    r = 0 
    for im in range(a):
        k = vec[im]
        if k != 0:
            r = r +1

    vecSon = np.zeros(r)
    for ik in range(r):
        vecSon[ik] = vec[ik+1]

    return vecSon, vec

# forexample1
a = 10%3
r = 13*13*9
s,k = divisibleList(r)
print (s, k )
# end of forexample1
