sbox = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]

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
