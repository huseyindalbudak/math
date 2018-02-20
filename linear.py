import numpy as np
#linear line is f(x) = ax +b for a and b is constant

#y = ax +b
#dy/dx  = a 

#x = [1,2,3,4] 

# x is order
# y is data set 
def linear(y): 
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
            
    return b
        
        
    
    


#not work now
    
    
y = [3,5,7,9]
print (linear(y))
#i = linear(y)
