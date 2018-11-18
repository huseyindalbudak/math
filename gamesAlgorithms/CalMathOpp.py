import numpy as np 

# this code is wrote for a game 
#the game: there are 4 number and 4 math opperation.
# we know 4 number and 2 loop. We need 3th loop resut 
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

def islemIter(sonuc,sonuc2):
    islemArray = ['topla', 'cikar','carp','bol']
    islemSirasi3 = np.random.randint(4)

    funcname3 = islemArray[islemSirasi3]
    sonuc3 =feval(funcname3,sonuc,sonuc2)
    
    return sonuc3, funcname3



def islem(x,y,z,l):
    islemSirasi = np.random.randint(4)
    islemArray = ['topla', 'cikar','carp','bol']
    funcname = islemArray[islemSirasi]
    sonuc = feval(funcname, x,y)
    islemSirasi2=np.random.randint(4)
    funcname2 = islemArray[islemSirasi2]
    sonuc2= feval(funcname2,z,l)
    #islemSirasi3=np.random.randint(4)
    sonuc3 = islemIter(sonuc,sonuc2)
    
    return sonuc2,sonuc,sonuc3,funcname,funcname2




bayrak = 1
a = 5
b = 6
c= 7
d = 4
#result 33
#while bayrak == 1:



funcSonuc = islem(a,b,c,d)
i = 0 

while bayrak==1:
    funcSonucRun = islem(a,b,c,d)
    son = funcSonucRun[2][0]
    print son
    if son ==33:
        print 'oldu iter',i
        print 'islem(a,b):',funcSonucRun[3]
        print 'islem2(c,d):',funcSonucRun[4]
        print 'islem3[(a,b),(c,d)]:',funcSonucRun[2][1]
        bayrak = 0
    else:
        i = i + 1 

#this while do not have to depend former
'''
a1= 4
b1= 4
c1= 9
d1= 3
#result 48

a2=3 
b2=2
c2=5
d2=1
#result ?
'''
