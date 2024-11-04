# So for any arbitary n , we have n variables with us and we can insert n-1 operators in between them.

# For operators we have two options : AND , XOR  ->  2**(n-1) options
# Also for variables we have option to choose between : 1 and 0 ->  2**(n) options

# So total number of permutations = 2**(n) * 2**(n-1) = 2**(2n-1)
# So for any n total number of permuations = 2**(2n-1)


# Code
def ans(n):
	var = 2
	var_perm = var**n
	op = 2
	op_perm = op**(n-1)
	total_perm = var_perm*op_perm
	print(total_perm)
	
ans(2)
ans(3)
ans(4)

n = int(input("Enter number of variables : "))
ans(n)
