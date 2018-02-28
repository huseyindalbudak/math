from sympy import *
import numpy as np


def deriv_symbolic(y,x):
    x = Symbol('x')
    yprime = y.diff(x)
    
    return yprime 

def second_deriv_symbolic(y,x): 
    x = Symbol('x')
    yprime = y.diff(x)
    yprime_prime = yprime.diff(x)
    
    return yprime_prime 

def local_peak(y,x,p):   # p is any point 
    x = Symbol('x')
    #y = fun(x)
    yprime = y.diff(x)
    
    if yprime == 0: 
        local_x = x
        local_y = y
        
    # it is must test for diffrent dataset
    return local_x , local_y

def similar_local_peak(y,x):
    local_cordinate = local_peak(y,x)
    e2 = local_coorinate[1]
    lis = np.zeros(np.size(y))
    for i in range(np.size(y)):    
        a = y[i]
        if e2 == a :
            similar_lis[i] = a
    return similar_lis


'''
# for example equation
y = x**2 + 1

yprime = deriv_symbolic(y,x)   #  y'   or dy/dx 
    
print (yprime)

yprime_yprime = second_deriv_symbolic(y,x)

print (yprime_yprime)
'''


def deriv_vec_numeric(x, y):
# ve would like tetha and betha for tangante 
    size_x = np.size(x)
    size_y = np.size(y)
    deriv_func= np.zeros(size_x)
    if size_x == size_y:
        for i in range(size_x-1):
            deriv_func[i] = np.float(x[i+1]-x[i])/(y[i+1]-y[i]) 
                
    else:
        return 'can not derivavtive'

    return deriv_func


'''
#  for example: deriv_vec_numeric function --->
x = [1,2,3,4,5,6,7,8,9]
y = [1,3,5,7,9,11,13,15,17]
print (np.diff(x)/np.diff(y))

a = deriv_vec(x,y)
print (a)
'''
