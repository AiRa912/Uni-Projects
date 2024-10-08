import numpy as np
def plu(A):
    
    #Get the number of rows
    n = len(A)
    
    #Allocate space for P, L, and U
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    P = np.eye(n, dtype=np.double)
    
    #Loop over rows
    for i in range(n):
        
        #Permute rows if needed
        for k in range(i, n): 
            if np.isclose(U[i,i], 0):
                break
            U[[k, k+1]] = U[[k+1, k]]
            P[[k, k+1]] = P[[k+1, k]]
            
        #Eliminate entries below i with row 
        #operations on U and #reverse the row 
        #operations to manipulate L
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
        
    return P, L, U

A = [[7, 3, -1], [3, 8, 1], [-1, 1, 4]]
plu(A)
print("A:", A)

