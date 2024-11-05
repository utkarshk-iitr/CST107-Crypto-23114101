from itertools import permutations
n = int(input("Enter n - "))

orig = []
for i in range(1<<n): orig.append(i)
perm = list(permutations(orig))

if n==1:
    print("2")
    exit()

count = 0

for v in perm:
    s = 0
    for i in range(n):
        f = ""
        for j in v:
            w = bin(j)[2:].zfill(n)
            f += w[i]
        # print(f)
        
        s1 = 0
        for j in range(n):
            for k in range(1<<n):
                # w = bin(k)[2:].zfill(n)[j]
                if f[k]!=f[k^(1<<j)]:
                    s1 += 1
                    break
        if s1==n:
            s += 1

    if s==n:
        count += 1
        
print("The count of functions is -",count)        