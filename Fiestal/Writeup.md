In fiestal cipher we divide the plaintext into two halves and they are being encrypted as per the rule,

l[i] = r[i-1]
r[i] =  l[i-1] xor k[i-1] xor r[i-1]

Round keys are generated by key scheduling

For decryption same this is to be done just the order of keys is reversed
