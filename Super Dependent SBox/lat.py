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

	for a in range(2 ** n):
		for b in range (2 ** m):
			e = str(L[a][b]).rjust(2)
			print(e, end=' ')
		print()
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
