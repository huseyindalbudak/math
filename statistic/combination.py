# 18.06.2018 h. Dalbudak

#it can use for huge number combination
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n,r):
    return factorial(n) /factorial(r) / factorial(n-r)
    
#for example 
#a = combination(50,10)
