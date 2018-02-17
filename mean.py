
#a is a vector 

def aritmatic(a):         #mean
    # if a input is array
    mean = sum(a)/len(a)
    return mean
         
def geometric_vec(a):    #mean
    num = np.size(a)
    k = 1 
    
    for i in range(num):
        k = k*a[i]
    
    geometricmean = k/num 
    return geometricmean
