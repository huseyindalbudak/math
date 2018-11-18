import numpy as np 
#python 2.7
#H.Dalbudak Now 18 2018
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
a1= 4
b1= 4
c1= 9
d1= 3



funcSonuc = islem(a,b,c,d)
i = 0 
im = 0

while bayrak==1:
    funcSonucRun = islem(a,b,c,d)
    son = funcSonucRun[2][0]
    print 'son',son
    if son ==33:
        print 'oldu iter i',i
        print 'islem(a,b):',funcSonucRun[3]
        print 'islem2(c,d):',funcSonucRun[4]
        print 'islem3[(a,b),(c,d)]:',funcSonucRun[2][1]
        isab = funcSonucRun[3]
        iscd = funcSonucRun[4]
        isfin = funcSonucRun[2][1]
        bayrak = 0
    else:
        i = i + 1

while bayrak == 0:
    funcSonucRun1 = islem(a1,b1,c1,d1)
    son1 = funcSonucRun1[2][0]
    print 'son1' , son1
    if son1 ==48:
        print 'oldu iter im',im
        print 'islem(a,b):',funcSonucRun[3]
        print 'islem2(c,d):',funcSonucRun[4]
        print 'islem3[(a,b),(c,d)]:',funcSonucRun[2][1]
        isab1 = funcSonucRun[3]
        iscd1 = funcSonucRun[4]
        isfin1 = funcSonucRun[2][1]
        if (isab==isab1)and{iscd==iscd1}and(isfin==isfin1):
            print 'islemler karsilikli'
            bayrak = 1
        print 'islemler karsiliklidegil'
        bayrak = 1

    else:
        im = im +1 

a2=3 
b2=2
c2=5
d2=1
result1 = feval(isab,a2,b2)
result2 = feval(iscd, c2,d2)
result3 = feval(isfin1,result1,result2)
print result3

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
