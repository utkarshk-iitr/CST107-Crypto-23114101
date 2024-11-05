sbox = {"0":"C", "1":"5", "2":"6", "3":"B", "4":"9", "5":"0", "6":"A", "7":"D", "8":"3", "9":"E", "A":"F", "B":"8", "C":"4", "D":"7", "E":"1", "F":"2"}
key = input("Enter key in 20 hex digits : ").upper()

k0 = key[:4]
k1 = key[4:8]
k2 = key[8:12]
k3 = key[12:16]
k4 = key[16:]

key = [k0,k1,k2,k3,k4]
wk0 = k0
wk1 = k1
wk3 = k3
wk4 = k4

def xor(a,b):
    a = int(a,16)
    b = int(b,16)
    c = a^b
    return hex(c)[2:].upper()

def Ffunc(r):
    r = r.zfill(4)
    arr = list(r)
    new = [0,0,0,0]
    for i in range(6):
        new[0] = xor(arr[1],sbox[arr[0][-1]])
        new[1] = arr[2]
        new[2] = xor(arr[3],sbox[arr[2][-1]])
        new[3] = arr[0]
        arr = new.copy()
    return "".join(arr)

rc = []
for i in range(36):
    u = "0"+bin(i)[2:].zfill(6)+"00"+bin(i)[2:].zfill(6)+"0"
    rc.append(hex(int(u,2)))

rk = []
for i in range(36):
    c = xor(key[i%5],rc[i]).zfill(4)
    rk.append(c)

def encrypt():
    pt = input("Enter plaintext in 16 hex digits : ").upper()
    pt = [pt[:4],pt[4:8],pt[8:12],pt[12:]]
    ct = [0,0,0,0]

    ct[0] = xor(xor(pt[1],rk[0]),Ffunc(xor(pt[0],wk0))).zfill(4)
    ct[1] = xor(pt[2],wk1).zfill(4)
    ct[2] = xor(xor(pt[3],rk[1]),Ffunc(xor(pt[2],wk1))).zfill(4)
    ct[3] = xor(pt[0],wk0).zfill(4)
    pt = ct.copy()
    
    for i in range(1,17):
        ct[0] = xor(xor(rk[2*i],pt[1]),Ffunc(pt[0])).zfill(4)
        ct[1] = pt[2].zfill(4)
        ct[2] = xor(xor(rk[2*i+1],pt[3]),Ffunc(pt[2])).zfill(4)
        ct[3] = pt[0].zfill(4)
        pt = ct.copy() 

    ct[0] = xor(xor(pt[1],rk[34]),Ffunc(pt[0])).zfill(4)
    ct[1] = xor(pt[2],wk4).zfill(4)
    ct[2] = xor(xor(pt[3],rk[35]),Ffunc(pt[2])).zfill(4)
    ct[3] = xor(pt[0],wk3).zfill(4)

    return "".join(ct)

def decrypt(cipher):
    ct = cipher
    ct = [ct[:4], ct[4:8], ct[8:12], ct[12:]]
    pt = [0, 0, 0, 0]

    pt[0] = xor(ct[3],wk3).zfill(4)
    pt[2] = xor(ct[1],wk4).zfill(4)
    pt[1] = xor(xor(ct[0],Ffunc(pt[0])),rk[34]).zfill(4)
    pt[3] = xor(xor(ct[2],Ffunc(pt[2])),rk[35]).zfill(4)
    ct = pt.copy()

    for i in range(16, 0, -1):
        pt[0] = ct[3].zfill(4)
        pt[2] = ct[1].zfill(4)
        pt[1] = xor(xor(rk[2*i], ct[0]), Ffunc(pt[0])).zfill(4)
        pt[3] = xor(xor(rk[2*i+1], ct[2]), Ffunc(pt[2])).zfill(4)
        ct = pt.copy()

    pt[2] = xor(ct[1], wk1).zfill(4)
    pt[0] = xor(ct[3], wk0).zfill(4)
    pt[1] = xor(xor(ct[0], rk[0]), Ffunc(xor(pt[0],wk0))).zfill(4)
    pt[3] = xor(xor(ct[2], rk[1]), Ffunc(xor(pt[2], wk1))).zfill(4)

    return "".join(pt)

cipher = encrypt()
print("Ciphertext :",cipher)
pl = decrypt(cipher)
print("Recovered plaintext : ",pl)
