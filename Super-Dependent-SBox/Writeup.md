We will first make all the possible permutations for F to create vectorial boolean functions.
Then we construct out fi from these vectors and then check if they are super dependent on n variables or not.

If they are dependent then we increment our count. The checking is done by nested loops including bitwise operations.
The overall time complexity is - (2**n)! * n*n * (2**n)
