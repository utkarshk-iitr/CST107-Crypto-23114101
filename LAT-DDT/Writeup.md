To compute LAT we first generate a blank array then LAT[i][j] = bias integer of i and j
Bias integer is calculated by mask a and b when a.x (xor) b.y = 0 , so LAT is computed

For DDT first generate a blank array then we run a nested loop for i and j
Here input is i^j and output is sbox[i]^sbox[j] ,
DDT[input][output] += 1 , Hence DDT is computed
