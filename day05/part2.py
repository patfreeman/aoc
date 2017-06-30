#!/usr/bin/env python

import hashlib
import sys

id="ugkcyxxp"
i=0
SPINNER_MOD=4500
spinner=["|","/","-","\\"]
password=[" "," "," "," "," "," "," "," "]
sys.stdout.write("".join(password) + "|")
while " " in password:
	md5 = hashlib.md5(id + str(i)).hexdigest()
	if md5[:5] == "00000":
		#print str(i) + " " + md5 + " " + "".join(password) + " " + md5[6]
		if ord(md5[5]) < 56:
			if password[int(md5[5])] == " ":
				password[int(md5[5])] = md5[6]
		sys.stdout.write("\r" + "".join(password) + " ")
		sys.stdout.flush()
	i += 1
	if not i % SPINNER_MOD:
		sys.stdout.write("\b")
		sys.stdout.write(spinner[(i/SPINNER_MOD)%len(spinner)])
		sys.stdout.flush()
sys.stdout.write("\r")
sys.stdout.write("".join(password))
sys.stdout.write("\n")
