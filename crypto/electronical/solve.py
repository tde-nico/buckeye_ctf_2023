import requests
import string

def encrypt(msg):
	url = 'https://electronical.chall.pwnoh.io'
	r = requests.get(url + '/encrypt', params={'message': msg})
	assert r.status_code == 200
	print(f'encrypt: {r.text=} {len(msg)=} {msg=}')
	return r.text

def calculate_stat_offset():
	base_len = len(encrypt('A' * 16))
	print(f'{base_len=}')
	for i in range(16, 32):
		msg = 'A' * i
		ct = encrypt(msg)
		if len(ct) != base_len:
			return i

def calculate_lookup_table(base):
	lookup_table = {}
	for c in string.printable:
		msg = (c + base).ljust(16, '\x00')
		ct = encrypt(msg)[0:32]
		lookup_table[ct] = c + base
	return lookup_table


start_offset = calculate_stat_offset()
print(f'{start_offset=}')

flag_end = ''

while True:
	if flag_end.startswith('bctf{'):
		print(flag_end)
		break

	lookup_table = calculate_lookup_table(flag_end)
	
	msg = (len(flag_end) + start_offset) * 'A'
	ct = encrypt(msg)[-96:-64]
	assert len(ct) == 32

	if ct in lookup_table:
		flag_end = lookup_table[ct]
		print(flag_end)
	else:
		print('Not Found')
		break

# bctf{1_c4n7_b3l13v3_u_f0und_my_c0d3b00k}
