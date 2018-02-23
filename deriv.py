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



'''
# for example equation
y = x**2 + 1

yprime = deriv_symbolic(y,x)   #  y'   or dy/dx 
    
print (yprime)

yprime_yprime = second_deriv_symbolic(y,x)

print (yprime_yprime)
'''
