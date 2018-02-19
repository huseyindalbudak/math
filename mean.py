
#a is a vector 

def aritmatic_mean(a):         #mean
    # if a input is array
    mean = sum(a)/len(a)
    return mean
         
def geometric_mean_vec(a):         #mean
    num = np.size(a)
    k = 1 
    
    for i in range(num):
        k = k*a[i]
    
    geometricmean = k/num 
    return geometricmean
