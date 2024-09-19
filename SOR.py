import numpy as np

def sor_solver(A,b,x0,w,maxiter):
  l=len(x0)
  sol=np.zeros(l)
  flag=0
  sr=0
  while flag<maxiter and sr<1:
      for i in range(0,l):
        sigma=0
        for j in range(0,l):
          if j!=i:
            sigma+=(A[i][j]*sol[j])
        sol[i]=((1-w)*sol[i])+((w*(b[i]-sigma)/A[i][i]))
      print("Iteration ", flag+1, "=", sol)
      flag+=1
  print("\n\nFinal Answer= ", sol)

A = np.array([[1, -2, 2],
              [3, 2, -4],
              [-5, 1, 4]])

b= np.array([8, -5, -6])

x0 = np.zeros(len(b))
maxiter=15
w=1
ans= sor_solver(A,b,x0,w,maxiter)



