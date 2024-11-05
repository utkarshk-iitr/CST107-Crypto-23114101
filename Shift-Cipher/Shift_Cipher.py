# Question-1
s = str(input("Enter uppercase string - "))
def UCText2Int(s):
    for i in s:
        k = ord(i)
        if 65<=k<=90:
            pass
        else:
            print("Enter uppercase string only")
            exit(0)

    li = [ord(i)-65 for i in s]
    print(li)
UCText2Int(s)


# Question-2
li = eval(input("Enter vector of intergers : "))
def Int2UCText(li):
    for i in li:
        if 0<=i<=25:
            pass
        else:
            print("Enter correct vector")
            exit(0)

    s = ""

    for i in li:
        s += chr(i+65)
    print(s)
Int2UCText(li)


# Question-3
ct = input("Enter ciphertext - ")
def decrypt(ct,key):
    s = ""
    for i in ct:
        p = (ord(i)-ord("A")-key)%26
        s += chr(p+65)
    print(s)

def countf(ct):
    d = {}
    for i in ct:
        if i not in d.keys():
            d[i] = 0
        d[i] += 1

    li = []
    for i in d.keys():
        li.append([d[i],i])
    li.sort()
    li.reverse()
    return li

li = countf(ct)
key = (ord(li[0][1]) - ord('E'))%26
print("Possible key -",key)
decrypt(ct,key)

choice = input("\nIs output correct (y,n) - ").lower()
if choice=="n":
    print()
    for i in range(26):
        print(i,end=" ")
        decrypt(ct,i)

# HXDALJAANBNAEJCRXWRBDWMNACQNWJVNSXWNB
# BCJHJCCQNARCIKDCYJATHXDALJAJCCQNFJUMXAO
# DWQYIDMCIFBSKGDODSFOHHVSTFCBHRSGYIBRSFHVSBOASXCBSG
# XLIHIXEMPWSJCSYVQIXXMRKAMPPFISRXLIWXSGOTEKIAVMXXIRMRGSHI
