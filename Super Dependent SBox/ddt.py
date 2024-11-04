def ddt(sbox,n,m):
	DDT = [[0]*2**m for i in range(2**n)]
	
	for i in range(2**n):
		for j in range(2**m):
			xin = i^j
			xout = sbox[i]^sbox[j]
			DDT[xin][xout] += 1
	
	for a in range(2 ** n):
		for b in range (2 ** m):
			e = str(DDT[a][b]).rjust(2)
			print(e, end=' ')
		print()
