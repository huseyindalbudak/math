def max_matrix(a):
    num = np.shape(a)
    numraw = num[0]
    k = np.zeros(numraw)
    for i in range(numraw):
        s = a[i]
        k[i] = max(s)
    maxi = max(k)
     # minimum number for the matrix elements
    return maxi

def min_matrix(a):
    num = np.shape(a)
    numraw = num[0]
    k = np.zeros(numraw)
    for i in range(numraw):
        s = a[i]
        k[i] = min(s)
    mini = min(k)
    # minimum number for the matrix elements
    return mini
