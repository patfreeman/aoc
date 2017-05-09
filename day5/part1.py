#!/usr/bin/env python

import hashlib

id="ugkcyxxp"
cnt=0
i=0
password=""
while cnt < 8:
	md5 = hashlib.md5(id + str(i)).hexdigest()
	if md5[:5] == "00000":
		print str(i) + " " + md5
		password = password + md5[5]
		cnt += 1
	i += 1
print password
