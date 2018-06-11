# the code is writed for non linear fitting 
# espeacially, it is similar method MATLAB code such as feval function
# H.Dalbudak 06.07.2018

def feval(funcName, *args):
    return eval(funcName)(*args)

def nlfit_deriv(mode1,beta,X,Y,n,nargin_nlfit,fun_struct):
    delta = np.zeros(np.size(beta))
    delta[n] = np.sqrt(np.finfo(float).eps ) * beta[n]

    if delta[n] == 0 :
        delta[n] = np.finfo(float).eps

    if nargin_nlfit >6:
        y1 = feval(mode1,beta+delta,X,fun_struct)
    else:
        y1 = feval(mode1, beta + delta, X)

    to_cal_dy_dbeta = y1-Y
    y = np.array(to_cal_dy_dbeta, dtype=float)/delta[n]

    while (np.sum(y) == 0) and (delta[n] < 0.01*beta):
        delta[n] = delta[n]*10

        if nargin_nlfit>0:
            y1 = feval(mode1, beta + delta, X, fun_struct)
        else:
            y1 = feval(model, beta + delta, X)

        to_cal_d = np.array(np.dot(np.sqrt(np.finfo(float).eps),beta[n]),dtype=float)
        y = np.array(to_cal_dy_dbeta , dtype=float)/to_cal_d

    return y
