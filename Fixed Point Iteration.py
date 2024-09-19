#Assignment Q1

import numpy as np
import matplotlib.pylab as m_plot


def fx(x):
    y=np.log(x)-(1/(x-1))
    return y

l=np.linspace(0,1, 100)

m_plot.plot(l, fx(l), linestyle='-', label='(0,1)')
m_plot.xlabel('x')
m_plot.ylabel('y')
m_plot.legend() 

'''
As the value of fx(0)*fx(1)<0, there surely exists a root, c (for c ∈(0,1)) where f(c)=0.
The value of c thus obtained is 0.08.

fx(x) is also differentiable in the given interval and fx'(x)<0 or fx'(x)>0 on the interval.
The solution obtained is unique in this interval

'''

k=np.linspace(2,3, 100)

m_plot.plot(k, fx(k), linestyle='-', label='(2,3)')
m_plot.xlabel('x')
m_plot.ylabel('y')
m_plot.legend()

'''
As the value of fx(2)*fx(3) not less than 0, there doesn't exists a root, c (for c ∈(2,3)) where f(c)=0.

Since there is no root in this interval, the uniqueness argument is invalid
'''
    
