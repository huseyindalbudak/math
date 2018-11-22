import numpy as np
'''
Nov 21 2018 | H.Dalbudak
----------------------------
last change Nov 22 2018
-if we know many number in the 3x3 sudo matrix, the program works properly with new function.
----------------------------
the codes is wrote for a 3x3 sudoku games
 rules: 
 -there are one 2D matrix. 
 -Row and col has not same number that are from 1 to 9.
 -the 3x3 matrix has not same number.
 -In additon to, if we know a number in the matrix, it should contunie properly with it.
method:
  - we full the matrix with random numbers   
  
'''
def matasu3x3(mat):
    rowcol = np.where(matsu>0)
    matsize = np.size(rowcol) #size =4 it means 2 index known 
    knownel = matsize/2
    rowarr = [0]*knownel
    colarr = [0]*knownel

    for i in range(knownel):
        rowarr[i] = rowcol[0][i]
        colarr[i] = rowcol[1][i]

    difnumarr = [0]*knownel
    
    for iy in range(knownel):
        difnumarr[iy] = mat[rowarr[iy]][colarr[iy]]
    
    arr = np.arange(1,10)
    ann = arr.tolist()
    akk = arr.reshape(3,3)
    akk = np.array(akk)
    for im in range(knownel):
        gecici = difnumarr[im]
        gecint = int(gecici)
        #print akk.index(gecint)
        ann.remove(gecint)
    
    np.random.shuffle(ann)
    arar = np.zeros([3,3])
    #I want to inset in a list with known index and then reshape
    for il in range(knownel):
        listindex = knownel*rowarr[il] + colarr[il] 
        #i multiple row with total col number because I want to convert to vector with real coordinate according to 3x3 matrix
        listnum   = difnumarr[il] 
        ann.insert(listindex, listnum)
    ann = np.array(ann)
    annSon = ann.reshape([3,3])

    return annSon

'''
#this func is for only one known number 
def matsu3x3(mat):
    #arr = 1 + np.random.randint(8) #because np.random.randint(a) produce from 0 to a-1 random integers 
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
'''

matsu = np.zeros([3,3])

##########
#forexample
matsu[0][2] = 4 #known index
matsu[1][1] = 7
matsu[2][1] = 3
at =np.where(matsu>0)
#########
cikti = matasu3x3(matsu)
print cikti
