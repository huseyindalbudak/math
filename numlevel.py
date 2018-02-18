'''
forexample
a = [[10,4] ,[2,11] ]
max(a)  is [10,4] but it is not true !!! 
we can find a numbe for any matrix with  max_matrix  function
it can important for the complex problems
'''

def max_matrix(a):
    num = np.shape(a)
    numraw = num[0]
    k = np.zeros(numraw)
    for i in range(numraw):
        s = a[i]
        k[i] = max(s)
    maxi = max(k)
    
    return maxi

def min_matrix(a):
    num = np.shape(a)
    numraw = num[0]
    k = np.zeros(numraw)
    for i in range(numraw):
        s = a[i]
        k[i] = min(s)
    mini = min(k)
    
    return mini
