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
    if y != 0:
        #bol =np.float(x)/y
        bol = x/y
    else:
        bol = 0
    return bol

def recEleman(el1,el2,funcname):
    print el1,funcname,el2

def tislem(args):

    #args = np.array(args)
    #args = args.tolist()
    numEleman = np.size(args)
    
    islemSirasi = np.random.randint(4)
    islemArray = ['topla', 'cikar','carp','bol']
    funcname = islemArray[islemSirasi]
    
    elemanSirasi1 = np.random.randint(numEleman)
    eleman1 = args[elemanSirasi1]
    args.remove(eleman1)
    
    elemanSirasi2 = np.random.randint(numEleman-1)
    eleman2 = args[elemanSirasi2]
    #print eleman1,eleman2,islemSirasi
    sonuc = feval(funcname, eleman1, eleman2)
    args.remove(eleman2)
    args.insert(0,sonuc)
    
    recEleman(eleman1,eleman2,funcname)

    return args


def dondur(girdi):
    num = 2 #for while loop it is not important 
    while num>1:
        girdi = tislem(girdi)
        num = np.size(girdi)
        #print girdi

    return girdi

bayrak =1
it = 0
while bayrak==1:
    girdi = dondur([13,12,3,4])
    print 'olmamis',girdi
    girdim = girdi[0]
    if girdim == 27:
        print 'oldu', girdim
        bayrak = 0
    else:
        it = it +1 
        bayrak = 1

print 'girdi',girdim
print 'total iteration',it

