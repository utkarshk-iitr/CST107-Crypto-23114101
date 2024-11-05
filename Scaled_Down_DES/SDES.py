key = input("Enter key in 12 bits : ")
ptext = input("Enter plaintext in 8 bits : ")

c0 = key[9]+key[3]+key[0]+key[4]+key[10]
d0 = key[7]+key[8]+key[2]+key[6]+key[1]
c1 = c0[1:]+c0[0]
d1 = d0[1:]+d0[0]
c2 = c1[1:]+c1[0]
d2 = d1[1:]+d1[0]

li = [8,2,4,9,7,10,6,3]
key1 = ""
key2 = ""
for i in li:
    key1 += (c1+d1)[i-1]
    key2 += (c2+d2)[i-1]
finalkey = [key1,key2]

def xor(a,b):
    a = int(a,2)
    b = int(b,2)
    return bin(a^b)[2:].zfill(8)

def encrypt2rounds(pt,key):
    nr = 2
    pt = pt[1]+pt[4]+pt[0]+pt[2]+pt[7]+pt[3]+pt[6]+pt[5]
    ct = pt

    for i in range(1,nr+1):
        ct = xor(key[i-1],ct)

    ct = ct[2]+ct[0]+ct[3]+ct[5]+ct[1]+ct[7]+ct[6]+ct[4]
    return ct

def decrpyt2rounds(ct,key):
    nr = 2
    ct = ct[1]+ct[4]+ct[0]+ct[2]+ct[7]+ct[3]+ct[6]+ct[5]
    pt = ct

    for i in range(1,nr+1):
        pt = xor(key[i-1],pt)
        
    pt = pt[2]+pt[0]+pt[3]+pt[5]+pt[1]+pt[7]+pt[6]+pt[4]
    return pt

ctext = encrypt2rounds(ptext,finalkey)
print("Ciphertext :",ctext)
prec = decrpyt2rounds(ctext,finalkey)
print("Recovered plaintext : ",prec)
