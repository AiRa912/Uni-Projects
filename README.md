A. THE FIXED ITERATION SERIES:
1. Root Finding and Function Analysis
Description:
Analyzes the function 
𝑓(𝑥)=log⁡(𝑥)−1𝑥−1
f(x)=log(x)− x−11
​to find and evaluate roots in intervals [0,1] and [2,3]. Includes plots and analysis to confirm root presence and uniqueness.

3. Fixed Point Iteration Method
Description:
Implements fixed-point iteration to find roots of 
𝑔(𝑥)=𝑒1/(𝑥−1)
g(x)=e 1/(x−1)
 . Includes functions for iteration and error tracking, with results showing convergence behavior.

4. Lipschitz Constant and Convergence Analysis
Description:
Calculates Lipschitz constants for 
𝑔(𝑥)=−𝑒1/(𝑥−1)(𝑥−1)2
g(x)=− (x−1) 2 e 1/(x−1)
 
​to assess convergence in intervals [0,1] and [2,3]. Analyzes function behavior and convergence criteria.

B. LU Decomposition(Gaussian)
Description:
Computes the LU decomposition of a square matrix 𝐴 with partial pivoting. The function returns the permutation matrix 𝑃, lower triangular matrix 𝐿, and upper triangular matrix 𝑈.

C. PLU Decomposition
Description: Performs PLU (Permutation-LU) decomposition of a matrix 𝐴. The function returns permutation matrix 𝑃, lower triangular matrix 𝐿, and upper triangular matrix 𝑈 after row permutations to ensure numerical stability.

D. Successive Over-Relaxation (SOR) Solver
Description: Solves a system of linear equations using the Successive Over-Relaxation (SOR) method. The function iteratively updates the solution vector 𝑥 to minimize the residual, based on a relaxation parameter 
𝑤 and a maximum number of iterations.




