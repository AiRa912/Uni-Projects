#Assignment Q4

import numpy as np
import random
import math

def func(x):
    return np.exp(1/(x-1))

def integrate(g, x0, tol,maxiter): #Values carry the same meaning as the previous question
    i = 0
    xn = []
    errn=[]
    for i in range(0,maxiter):
       x1=g(x0)
       xn.append(x1)
       err=abs(x1-x0)
       errn.append(err)
       x0=x1
       i+=1
       if err<tol:
           break

    print("\nList of Iterations:", xn)
    print("\nList of Errors: ", errn)

def g1(x):
    return -(np.exp(1/(x-1)))/((x-1)**2)

lmb=-g1(2)

def G1(x):
    return (np.exp(1/(x-1))+lmb*x)/(1+lmb)

integrate(G1,2.8,0.001,13)

def lip_func(x): #Values carry the same meaning as the previous question
    g=(-(np.exp(1/(x-1)))/((x-1)**2)+lmb)/(1+lmb)
    gabs=abs(g)
    L=np.max(gabs)
    x0=(random.choice(x))
    if L<1:
        print("\n\nLipschitz condition is satisfied. L=", abs(L))
        print("The function is CONVERGENT!")
        n_iter=int(math.log(((1-L)*(10**(-6))))/math.log(L))
        print("The maximum number of iterations needed= ", n_iter)
        integrate(func, x0, 0.000001 ,50)
    else:
        print("\n\nLipschitz condition isn't satisfied! L=", L)
        print("The function is DIVERGENT!")
        integrate(func, x0, 0.000001 ,13)


x2=np.linspace(2,3,10)
lip_func(x2)