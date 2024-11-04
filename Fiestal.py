key = input("Enter key in hex : ")
key = bin(int(key,16))[2:]
ptext = input("Enter plaintext : ")

def xor(a,b):
    a = int(a,2)
    b = int(b,2)
    return bin(a^b)[2:].zfill(4)

def encrypt3rounds(pt,key):
    nr = 3
    k1 = xor(key[0:4],key[4:8])
    k2 = xor(key[8:12],key[4:8])
    k3 = xor(key[0:4],key[8:12])
    k = [k1,k2,k3]
    
    pt = bin(int(pt,16))[2:]
    l = [pt[0:4]]
    r = [pt[4:8]]

    for i in range(1,nr+1):
        l.append(r[i-1])
        u = xor(l[i-1],xor(k[i-1],r[i-1]))
        r.append(u)

    ct = hex(int(r[nr]+l[nr],2))[2:].upper()
    return ct

def decrypt3rounds(ct,key):
    nr = 3
    k1 = xor(key[0:4],key[4:8])
    k2 = xor(key[8:12],key[4:8])
    k3 = xor(key[0:4],key[8:12])
    k = [k1,k2,k3]
    k.reverse()
    
    ct = bin(int(ct,16))[2:]
    l = [ct[0:4]]
    r = [ct[4:8]]

    for i in range(1,nr+1):
        l.append(r[i-1])
        u = xor(l[i-1],xor(k[i-1],r[i-1]))
        r.append(u)

    pt = hex(int(r[nr]+l[nr],2))[2:].upper()
    return pt

ctext = encrypt3rounds(ptext,key)
print("Ciphertext :",ctext)
ptext = decrypt3rounds(ctext,key)
print("Recovered plaintext :",ptext)