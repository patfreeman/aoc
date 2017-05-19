#!/usr/bin/env python

import hashlib

id="ugkcyxxp"
i=0
password=""
while len(password) < 8:
	md5 = hashlib.md5(id + str(i)).hexdigest()
	if md5[:5] == "00000":
		print str(i) + " " + md5
		password = password + md5[5]
	i += 1
print password
