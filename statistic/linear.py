import numpy as np
#linear line is f(x) = ax +b for a and b is constant
# x is order
# y is data set 
def linear_vec(y): 
    y_size = np.size(y)
    a = np.zeros(y_size-1)
    #for i in range(x_size):
    #    x[i] = i
    #x is order now 
    #need dy/dx
    b = np.zeros(y_size -1 )
    for i in range(y_size-1):
        a[i] = y[i+1]-y[i]
        if i < (y_size-2):    
            m = np.float(a[i])
            s = np.float(a[i+1])
            if m != s:
                b[i] = -1
            else:
                b[i] = +1 
    #it is not ready now
    return b
        
        
def devide_vec(y,x):
    y_size = np.size(y)
    x_size = np.size(x)
    z = np.zeros(y_size)
    if y_size == x_size:
        for i in range(y_size):
            z[i] = np.float(y[i])/x[i]
    
    return z 


def crossProduct_vec(y,x):
    y_size = np.size(y)
    x_size = np.size(x)
    z = np.zeros(y_size)
    if y_size == x_size:
        for i in range(y_size):
            z[i] = np.float(y[i])*x[i]
    
    return z 
        
def line(xvec,a,b):
    #to line produce
    size = np.size(xvec)
    y = [0]*size
    for i in range(size):
        y[i] = a*xvec[i] + b
    return y


#xvec = [5,7,8,9,10,11,12,13]
#y = line(xvec,3,9)
#print y

    
#not work now

#for example 
#y = [3,5,7,9]
#print (linear(y))
#i = linear(y)
    
    
