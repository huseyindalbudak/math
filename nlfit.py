import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
from scipy import stats, linalg

#Huseyin DALBUDAK
# NOV. 11 .2017
# non-linear gauss fitting

def feval(funcName, *args):
    return eval(funcName)(*args)

def fitresult( iter,sse,lambda_,n,p,yfit,r,sig,J):
    iterations = iter
    phi = sse
    lambda_ = lambda_
    NumPts = n
    NumParam = p
    yfit = yfit
    residual = r
    sigma = sig
    J = J
    return iterations,phi,lambda_,NumPts, NumParam,yfit,residual,sigma,J


def gaussfit(n,X):
    Amp = abs(n[0][0])
    Xc = n[1][0]  # fuc a gelen beta shape = (1,4)
    width = abs(n[2][0])
    backgnd = n[3][0]


    cikti_list = np.zeros([np.size(X), 1])

    for i in range(np.size(X)):
        cikti_list[i][0] = Amp * (np.exp(-1 * (X[i][0] - Xc) ** 2 / (width ** 2))) + backgnd

    return cikti_list


def nlfit_deriv(mode1, beta, X, Y, n, nargin_nlfit, *args):
    #A = np.array([[0, 1, 2, 3]])
    #k = 3  # kanin her elemani icin denenmemli


    # def nlfit_deriv(mode1, beta, X, Y, n, nargin_nlfit, *args):
    # n is A[k] elemani
    Y_fit = Y
    A_size = np.size(A)
    Y_fit_size = np.size(Y_fit)
    ymm = np.zeros([Y_fit_size,A_size])
    y1 = np.zeros([A_size,Y_fit_size])


    #n = A[0][k]  # kanin her elemani icin denenmemli

    beta_shape_col = np.size(beta)
    beta_shape_raw = np.size(beta[0])
    delta = np.zeros([beta_shape_col, beta_shape_raw])

    n_size = np.size(n)
    # for n in range(n_size):
    delta[n][0] = np.sqrt(np.finfo(float).eps) * beta[n][0]


    if delta[n] == 0:
        delta[n] = np.finfo(float).eps

    if nargin_nlfit > 6:
        y1 = feval(mode1, beta + delta, X, args)
    else:

        y1 = feval(mode1, beta + delta, X)


    to_cal_dy_dbeta = y1 - Y_fit


    delta_size = np.size(delta)
    Y_fit_size = np.size(Y_fit)
    y = np.zeros([Y_fit_size, delta_size])
    y_deneme =np.zeros([Y_fit_size,delta_size])
    # y[n] = np.array(to_cal_dy_dbet, dtype=float) / delta[n]
    #k = np.array(to_cal_dy_dbeta, dtype=float) / delta[0]
    for m in range(Y_fit_size):
        y[m][n] = (y1[m] - Y_fit[m]) / delta[n][0]
        y_deneme[m][n] = y1[m]-Y_fit[m]
    #y = (y1 - Y_fit)/delta[n][0]
    # print ' while oncesiit is y in nilfit_deriv ', y
    # print ' while oncesiit is y shape in nilfit_deriv ', np.shape(y)

    ### bu ornekte while hic girmiyor matlab shortcut demesinin sebebi o
    while (np.sum(y) == 0) and (delta[n] < 0.01 * beta):
        delta[n] = delta[n] * 10
        if nargin_nlfit > 0:
            y1 = feval(mode1, beta + delta, X, args)
        else:
            y1 = feval(mode1, beta + delta, X)

        to_cal_d = np.array(np.dot(np.sqrt(np.finfo(float).eps), beta[n]), dtype=float)
        y = np.array(to_cal_dy_dbeta, dtype=float) / to_cal_d

        # a = np.array(y,dtype= float)  #kod aktif degil kontrol amacli
        # print ''
        # print 'y shape for a  in nilfit_deriv' , np.shape(a)
    # y_arr = np.array(y,dtype=float)
    # y_size = np.size(y)
    # return y
    return y

def arafun(*args):
    y1 = feval(mode1, beta + delta, X)
    return args


def nlparci(*args):                  #nlparci(x,f,J,A):
    ################ bu silinecek  ######

    x = args[0]
    f= args[1]
    J=args[2]
    A=args[3]
    nargin = len(args)



    if nargin < 3:
        error('requires 3 input')

    f = np.array(f)
    f = f.reshape((-1, 1))

    # J is not vector then we can not np.size because it provide only number of element
    # not use [m,n] = np.size[J]
    m = len(J)  # number of row
    n = len(J[0])  # number of column


    if m <= n:
        errors('The length of x must equal the number of columns in J.')

    temp = np.where(np.max(np.abs(J)) == 0)

    if np.size(temp) != 0:
        J[temp][:] = J[temp][:] + np.sqrt(np.finfo(float).eps)

        # syntax in matlab qr is Orthogonal-triangular decomposition [Q,R] = qr(A)
        # syntx in python


    # Q, R =linalg.qr(J, mode='economic')
    Q, R = linalg.qr(J, mode='economic')


    # raw,col = np.shape(R)
    # J_size = np.size(J)/np.size(J[0])

    to_cal_eyesize = np.eye(np.size(R) / np.size(R[0]))

    Rinv = np.linalg.solve(R, to_cal_eyesize)


    # syntax in matlaba \ b <---> in py =>  linalg.solve(a,b)
    diag_info = np.zeros(np.size(Rinv[0]))
    carpim = Rinv * Rinv

    for i in range(np.size(Rinv[0])):
        # diag_info[i] = np.sum(carpim[0][i])
        diag_info[i] = np.sum(carpim[i])

    v = m - n
    f = np.array(f, dtype=float)
    rmse = np.sqrt(np.sum(f * f) / v)

    # .* symbol in matlab    <------> I use for loop
    # tinc(a,b) funcion in matlab mean Student's t distribution  in statistical method
    st_dist = stats.t.ppf(0.8413, v)

    delta = np.zeros(np.size(A))

    # for i in range(np.size(A)):
    delta[A] = np.sqrt(diag_info) * (rmse * st_dist)  # stats.t.ppf code is controlled via matlab


    return delta

# x,y,mode1,beta0,varargin  are must be send to function Even if it is an empty cluster


def nlfit0(X,y,mode1,beta0, *args ):
#def nlfit0( ):              # for nargin function
#*args fazladan girilenler icin args oalrak tanimlaniyor ornek mask ve dA
#*args mean in matlab that is varargin
#     print beta0
    #print 'it is varargin', varargin
    #matlabda varargin satirlara isleniyor [1,1]  [1,2] gibi
    #variables ======   matlab varargin  -------> python args
    #bu calismaya ozgu
    # args[0] = mask
    # args[1] = dA
    IterationPrint = 1
    a = np.ones(np.size(beta0))

    #print 'it is args' , args
    sig = np.sqrt(y)

    #print len(args)
    nargin = 4 + len(args)   # 4 input kesin var + args

    size_beta0= np.size(beta0)
    #print size_beta0
    if nargin == 5 :
        a = args[0]   # must be cell array in python any list
    if nargin == 6 :
        a = args[0]
        sig=args[1]
        if a == []:                # isempty in matlab --> code is tested
            a = np.ones(size_beta0)

    #print 'it is beta0' , beta0
    if nargin == 7 :
        a = args[0]
        sig = args[1]
        fun_struct = args[2]

        if a == []:
            a = np.ones(size_beta0)
            sig = np.sqrt(y)
    n = len(y)
    #print 'it is y' , y

# bu error kosuluna gerek gormedim simdilik
    #if np.size(y)  != 1:  # np.min kaldirildi
    #    errors('Requires a vector second input argument')
    #    print 'Requires a vector second input argument'


    # to colomise  but it turn the array !
    X = np.array(X)
    X = X.reshape((-1, 1))

    y = np.array(y)
    y = y.reshape((-1, 1))

    beta0 = np.array(beta0)
    beta0 = beta0.reshape((-1, 1))

    sig = np.array(sig)
    sig = sig.reshape((-1, 1))

    # find funtion oparation it use also find  nonzero element
    # find(sig==0) in matlab mean sig = 0 location in vector
    # it turn from 0 to infinity
    #sig(np.where(sig==0)) = float('inf') ---> is not work
    j_var = np.where(sig == 0)  # j is not array
    l_var = np.array(j_var)
    sig[l_var] = float('inf')

    #matlab find(a) means indicates of non-zero elements
    #####################################################
    #print 'it is a ',a
    if a != 0 :
        A = np.where(a)   # A shape (1,4) in matlab then attention
    #A = np.zeros(np.size(A))
    #for imm in range(np.size(A)):
    #    A[imm] = A_ass[0][imm]


    #matlab daki gibi kullanmak icin A[0] kolonunu kullanmak gerek

    #print 'it is A' , A
    p = len(A[0])
    J =np.zeros([n,p])
    M =np.zeros([n,p])  # sonra islem yapmak ixin
    beta = beta0
    betanew = np.zeros(len(np.array(A[0])))
    betaLM = beta0
    betanew = beta * 1.01           # matrix elementi gostermeye gerek yok

    # strcmp in matlab if mode1 ='twoaxis'  ---> 1 or true  else  0 or false

    if mode1 == 'twoaxis':
        maxiter = 10
    else:
        maxiter = 100

    iter = 0
    betatol = 1e-4
    rtol = 1e-4
    sse = 1.0
    sseold = 1
    lambda_=0.01
    #~ symbol in matlab is not equal then we can use != []
    # \ symbol is next line for same code to read easy
    #a & b or and(a,b)	logical_and(a,b) or a and b	Element-wise logical AND
    #a | b or or(a,b)	logical_or(a,b) or a or b	Element-wise logical OR


    im = 0  #deneme amacli
    print 'maxiter line 299' , maxiter
# ~ isempty in matlab mena np.size(A) = 0
    kosul12    = np.size(np.sum((np.array(betanew-beta)/np.array(beta + np.sqrt(np.finfo(float).eps))) ) > betatol) !=0 \
            or ((((sseold-sse)/(sse + np.sqrt(np.finfo(float).eps)))) > rtol)
    kosul3 = iter < maxiter
    #while 1. kosul icin sifir olmayan elemanlari >betatol olacak simdilik sum kullaniyorum
    #while (np.sum((np.array(betanew-beta)/np.array(beta + np.sqrt(np.finfo(float).eps))) ) > betatol) \
    #        | ((((sseold-sse)/(sse + np.sqrt(np.finfo(float).eps)))) > rtol)   \
    #        & (iter < maxiter):
            # ornektde ordan oncesi 0 cikiyor matlabda
    bayrak = 1    # test amacli sonra silinecek
    km =0
    while kosul12 and kosul3 and (bayrak ==1):
        print '__1. while girdi__'    #ornekde matlabda girdi

        print 'simdi durdu !'      ## uyari
        # for pause function in matlab is temporarily stop            print 'bekleyiniz'          ## uyari
        #time.sleep(0.0001)
        print 'biraz daha bekleyiniz'  ## uyari

        if iter > 0:
            print 'beta iter line 320' ,beta
            beta = betanew


        iter = iter +1
        print 'iter line 324', iter
        if IterationPrint :          #maybi   IterationPrint == 1  is true but why use we the condition   #control -->   if case can npt define main code
            # There are not condition main matlab code !!!
            print 'iteration', iter, 'chai_square', sse / (n - p)

        if nargin >6:
            yfit = feval(mode1,beta,X,fun_struct)
        else:
            yfit = feval(mode1,beta,X)


            #chisqure opreation
        to_cal_resudal = y-yfit

        r = to_cal_resudal / sig
        # a'*b in matlab  ---->  vector icin (a[np.newaxis, :].T ) * b   in python
            # a'*b in matlab  ---->  np.dot(np.transpose(c) , c)  matrix icin
        sseold_ = (r[np.newaxis,:].T) * r          #matlabda dot produc isteniyorsa np.sum(np.diag(s))  kodu kullanilabilir
        sseold = np.sum(sseold_)


        J_size = np.size(J)/np.size(J[0])   #column sayisini bulmak icin

        var =[[],[],[],[]]

        for k in range(p):
            if nargin > 6 :
                J[:][k] = nlfit_deriv(mode1,beta,X,yfit,A[0][k],nargin,fun_struct)/sig # fun_struct
                print '1.while j[][] kosulu nargin>6 '
            else:

                variables_ = 'nanelik'


                n_tot = n
                J_T = np.transpose(J)
                M = nlfit_deriv(mode1, beta, X, yfit, A[0][k] , nargin)
                for imm in range(np.size(yfit)):
                    J[imm][k] = M[imm][k]
        JJ = np.dot(np.transpose(J),J)
        ## JJ  ++++

        Jr = np.dot(np.transpose(J),r)
        step_sol =np.multiply(JJ,(np.eye(p)*(1+lambda_)))
        step_sol_2 = JJ-np.diag(np.diag(JJ))
        stepLM = np.linalg.solve((step_sol_2 +step_sol),Jr)
        betaLM[A] = beta[A] + stepLM   ## suan yanlis !!! while tamamlaninca kontrol et


        if nargin > 6 :
            yfitnew = feval(mode1,betaLM,X,fun_struct)
        else:
            yfitnew = feval(mode1,betaLM,X)
            ###### s0 = np.around(matrix , decimals=1)

            #to_cal_resudal_2 =np.around(y,decimals=1) - np.around(yfitnew,decimals=1)
        to_cal_resudal_2 = y-yfitnew

        rnew = np.array(to_cal_resudal_2,dtype=float) / sig

        sseLM = np.dot(np.transpose(rnew),rnew)

        iter1 =0

            # (sseLM > sseold) and (iter1 < 12): kosulunua bu ornekte girmiyor !! sonra kontrol
            #print 'it is iter', iter1
        #          print 'sseLM' , sseLM[0][0]

            #print 'sseold', np.sum(sseold)
        kosul_iter_1 = iter1 < 12
        kosul_iter_2 = sseLM[0][0] > sseold
        while kosul_iter_1 & kosul_iter_2 :
            print 'while girdi line 407l'
            stepLM = np.array(stepLM,dtype=float)/np.sqrt(10)
            betaLM[A] = beta[A] + stepLM
            if nargin > 6:
                yfitnew = feval(mode1, betaLM, X, fun_struct)
                print 'line 410 kosul nargin>6'
            else:
                yfitnew = feval(mode1, betaLM, X)

            #to_cal_resudal_2 = y - yfitnew
            to_cal_resudal_2 = y-yfitnew
            rnew = np.array(to_cal_resudal_2,dtype=float) / sig
            sseLM =  rnew*rnew_cl
            iter1 = iter1 +1

        if iter1 < 12:
            lambda_ = lambda_/2
            betanew = betaLM
            sse     =sseLM
        else:
            lambda_ = lambda_*10


        if iter == maxiter:
            print 'NLINFIT did NOT converge. Returning results from last iteration.'

        chisquare = sse / (n - p)

        fitresult = [iter, sse,lambda_,n,p,yfit,r,sig,J]


        errors=nlparci(beta[A], r, J, A)
        #bayrak = 0 ## testing   ----->  sonra sil
        #gecici***********************
        if iter == 10000:
            bayrak=0
        #************************


    return beta,chisquare,errors,fitresult , yfit




filem = open('veri.txt','r')
sart = 1
column_sayisi = 7

b = np.loadtxt('veri.txt')
sayisi = np.size(b)
raw_sayisi = sayisi/column_sayisi
q = np.zeros(raw_sayisi)

bayrak = 1
m=0

#np.loadtxt vektore cevirirken ki durumu duzeltmek icin
for i in range(0,raw_sayisi*column_sayisi,7):
    q[m] = b[i]
    m =m+1

k = np.loadtxt('veri.txt')
s= 0
A = np.zeros(raw_sayisi)

for nm in range(0,raw_sayisi*column_sayisi-6,7):
    A[s] = k[nm+6]
    s = s+1

dA = np.sqrt(A)
#print 'it is dA' , dA
n2=[3000,0.22,0.01,100];
mask=[1, 1, 1, 1];
[nuvefit,chisquare,errors,fitresult,yfit] = nlfit0(q,A,'gaussfit',n2,mask,dA)


plt.plot(q,A,'*')
plt.errorbar(q,A,yerr=dA,fmt='ob')
plt.plot(q,yfit, label= 'it is n 2')
plt.show()
