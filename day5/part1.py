#!/usr/bin/env python

import hashlib
import sys

id="ugkcyxxp"
i=0
SPINNER_MOD=4500
spinner=["|","/","-","\\"]
password=""
while len(password) < 8:
	md5 = hashlib.md5(id + str(i)).hexdigest()
	if md5[:5] == "00000":
		#print str(i) + " " + md5
		password = password + md5[5]
		sys.stdout.write("\r")
		sys.stdout.write(password)
                sys.stdout.flush()
	i += 1
	if not i % SPINNER_MOD:
                sys.stdout.write("\b")
                sys.stdout.write(spinner[(i/SPINNER_MOD)%len(spinner)])
                sys.stdout.flush()
sys.stdout.write("\r")
print "".join(password)
