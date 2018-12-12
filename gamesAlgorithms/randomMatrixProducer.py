#python 3.7

import numpy as np
#it is for any dimention squre matrix 
# the matrix has random distribution accoring to matrix row(or col) size
def order(k):
    s = np.zeros(k)
    for i in range(k):
        s[i] =i+1 
    return s

def mixer(an):
    #an is a vector
    #it is mixer for another vecor. it is different than numpy-->random-->shuffle
    np.random.shuffle(an)
    size = np.size(an)
    lale = np.zeros(size)
    for i in range(size):
        lale[i] = an[i] 

    return lale

def nane(a):
    #a is square matrix dimendion
    sizem = np.shape(a)
    sizer = sizem[0]
    sizec = sizem[1] 
    if sizer != sizec:
        print ('error ---> it is not a square materix')
    else:
        print('it is good')
    rowj = [[]]*sizer
    rowi = np.zeros(sizer)
    #print (rowj[1])

    #rowm = np.zeros([0,sizer])
    for im in range(sizer):
        lis = order(sizer)
        rowi = mixer(lis)
        print ('it is for rowi',rowi)
        print (rowj[im])
        rowj[im] =rowi
    return rowj
#print (np.random.randint([1,8]))

def lister(k):
    #k is a number for one side of squre dimention 
    #the forction produce squre mateix acoording to k dimention
    rowj = order(k)
    rowjm = [[]]*k
    for i in range(k):
        rowjm[i] = rowj
    return rowjm
    #for i in range(k)

#####################forexample:  we need 10x10 matrix with random integer distribution from 1 to 10 ###############
km = lister(10)       
r = nane(km)
####################
print (r)
