#Assignment Q3

import numpy as np
import random
import math
def func(x):
    return np.exp(1/(x-1))

def integrate(g, x0, tol,maxiter):  #Values carry the same meaning as the previous question
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


def lip_func(x):
    '''
    To find the Lipschitz constant

    Parameters
    ----------
    x: float
       the array of values within the given interval

    Returns
    -------
    If the Lipschitz condition is satified,
       -Lipschitz constant ; float
       -the maximum number of iterations needed for convergence; integer
       -the iterates, errors and order of convergence; lists
    
    If the Lipschitz condition is not satisfied,
       -Lipschitz constant; float (greater than 1)
    
    '''
    g=-(np.exp(1/(x-1)))/((x-1)**2)
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
    
#For the first interval
print("For the interval [0,1]")
x1=np.linspace(0,0.99999,10)
lip_func(x1)

#In this interval, as more iterations are getting calculated, the lower is the error value, showing that the function is converging at its root value, xc= 0.259246; with upto 6 decimel accuracy.

#For the second interval
print("\n\nFor the interval [2,3]")
x2=np.linspace(2,3,10)
lip_func(x2)

#In this interval, the error value is increasing with more iterations, even reaching infinity, showing that the function is divergent in the given interval.