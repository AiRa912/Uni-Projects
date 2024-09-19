#Assignment Q2
import math 
# Define the function.
def integrate(g, x0, tol,maxiter):
    '''
    Use the fixed point iteration method to find the roots of f(x).

    Parameters
    ----------
    g    : function
           Function to evaluate x on.
    x0   : float
           First initial value.
    tol  : float
           Tolerance used for stopping the iteration.
    maxiter : float
              maximum number of iterations allow

    Returns
    -------
    3 lists
    
    xn   : all values of the iterates
    errn : error measured
    ordn : an "experimental" measure of order of order scheme
    
    '''
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

    print("List of Iterations:", xn)
    print("\nList of Errors: ", errn)

# Define a test function.
def polynomial(x):
    return math.exp(1/(x-1))

x0 = 0.60
tol = 0.000001
maxiter=50

y = integrate(polynomial, x0, tol, maxiter)


