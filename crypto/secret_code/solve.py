import pwn

flag = '1:10:d0:10:42:41:34:20:b5:40:03:30:91:c5:e1:e3:d2:a2:72:d1:61:d0:10:e3:a0:43:c1:01:10:b1:b1:b0:b1:40:9'
key = 'snub_wrestle'

flag = flag.replace(':', '')
flag = bytes.fromhex(flag)

flag = pwn.xor(flag, key)

print(flag)

# bctf{d0n't_lo0k_uP_snub_wResTling}
