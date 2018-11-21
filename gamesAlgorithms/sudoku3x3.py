import numpy as np
'''
Nov 21 2018 | H.Dalbudak
the codes is wrote for a 3x3 sudoku games
 rules: 
 -there are one 2D matrix. 
 -Row and col has not same number that are from 1 to 9.
 -the 3x3 matrix has not same number.
 -In additon to, if we know a number in the matrix, it should contunie properly with it.
method:
  - we full the matrix w'th random numbers   
'''

#def mixsum(arri,arrl):


def matsu3x3(mat):
    #arr = 1 + np.random.randint(8) #because np.random.randint(a) produce from 0 to a-1 random integers 
    bayrak = 1
    rowcol = np.where(matsu>0)
    row = rowcol[0] # row and col can be array thus it should be process a functioni
    col = rowcol[1]
    difnum = mat[row[0]][col[0]] #it can be array again

    #difnums index in totvec is row[0]+col[0]
    difnumin = row[0]+col[0] 
    arr = np.arange(1,10)
    np.random.shuffle(arr) # arr order mixed 
    #print m, arr 
    
    arri = np.arange(1,difnum)
    arrl = np.arange(difnum+1,10) 
    np.random.shuffle(arri)
    np.random.shuffle(arrl)
    aravec = arri.tolist() +arrl.tolist()
    
    difnum = np.float(difnum)
    aravec.insert(difnumin,difnum)
   
    matsize2 = np.shape(mat)
    matsize = matsize2[0]
    aravec = np.array(aravec)
    totmat = aravec.reshape(matsize,matsize)
    return totmat


matsu = np.zeros([3,3])

##########
#forexample
matsu[0][2] = 4 #known index
at =np.where(matsu>0)
#########
cikti = matsu3x3(matsu)
print cikti
