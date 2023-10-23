import pyshark
import base64

cap = pyshark.FileCapture('./frames.pcap')

for pkt in cap:
	ssid_b64 = pkt['WLAN.MGT'].wlan_ssid
	ssid = base64.b64decode(ssid_b64)
	if b'bctf{' in ssid:
		print(ssid)
		break

# bctf{tw0_po1nt_4_g33_c0ng3s7i0n}
