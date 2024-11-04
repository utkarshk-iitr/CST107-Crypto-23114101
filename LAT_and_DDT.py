# LAT
def dot(U, V):
	W = U & V
	dot = 0
	while W != 0:
		dot ^= W & 1
		W >>= 1
	return dot

def bias_integer(S, a, b, n):
	e = 0
	for x in range(2 ** n):
		if dot(a, x) == dot(b, S[x]):
			e += 1
	return e - 2 ** (n - 1)

def lat(S, n, m):
	L = [[0] * (2 ** m) for _ in range(2 ** n)]
	for a in range(2 ** n):
		for b in range(2 ** m):
			L[a][b] = bias_integer(S, a, b, n)
	return L

def print_lat(L, n, m):
	m1,m2 = 0,0
	for a in range(2 ** n):
		for b in range (2 ** m):
			m1= max(L[a][b],m1)
			m2= min(L[a][b],m2)
			e = str(L[a][b]).rjust(2)
			print(e, end=' ')
		print()
	return m1,m2

H = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]
L = lat(H, 4, 4)
m1,m2 = print_lat(L, 4, 4)
print("Max entry =",m1)
print("Min entry =",m2)


# DDT
sbox = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]
DDT = [[0]*16 for i in range(16)]
for i in range(2**4):
	for j in range(2**4):
		xin = i^j
		xout = sbox[i]^sbox[j]
		DDT[xin][xout] += 1

for i in DDT:
	print(i)
