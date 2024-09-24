from lat import lat
from ddt import ddt

def func(n):
    li = []
    for i in range(2**n):
        b = bin(i)[2:].zfill(n)
        li.append(b)
    
    w = []
    for i in range(2**(n-1)):
        b = bin(i)[2:].zfill(n-1).replace('0','A').replace('1','X')
        w.append(b)
        
    for j in w:
        sbox = []
        for i in li:
            p = int(i[0],2)
            for a, b in zip(i[1:],j):
                if b=='A':
                    p &= int(a,2)
                else:
                    p ^= int(a,2)
            sbox.append(p)
        
        print("S-Box : ",sbox)
        print("---------- LAT ----------")
        lat(sbox,n,n)
        print("---------- DDT ----------")
        ddt(sbox,n,n)
        print()
        print()

func(4)