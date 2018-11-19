import numpy as np 

# this code is wrote for a Bir Kelime Bir Islem game
# It estimates the math operation among many number with respec to a result

def feval(funcName, *args):
    return eval(funcName)(*args)

def topla(x,y):
    toplam = x+y
    return toplam

def cikar(x,y):
    cikarim = x-y
    return cikarim

def carp(x,y):
    carp = x*y
    return carp

def bol(x,y):
    bol = x/y
    return bol
    
def tislem(*args):
    args = np.array(args)
    args = args.tolist()
    numEleman = np.size(args)
    
    islemSirasi = np.random.randint(4)
    islemArray = ['topla', 'cikar','carp','bol']
    funcname = islemArray[islemSirasi]
    
    elemanSirasi1 = np.random.randint(numEleman)
    eleman1 = args[elemanSirasi1]
    args.remove(eleman1)
    
    elemanSirasi2 = np.random.randint(numEleman-1)
    eleman2 = args[elemanSirasi2]
    print eleman1,eleman2,islemSirasi
    sonuc = feval(funcname, eleman1, eleman2)
    args.remove(eleman2)
    args.insert(0,sonuc)

    return args


cikti = tislem(13,12,3,4)
print cikti 
