#!/usr/bin/env python

import hashlib
import sys

id="ugkcyxxp"
i=0
password=[" "," "," "," "," "," "," "," "]
while " " in password:
	md5 = hashlib.md5(id + str(i)).hexdigest()
	if md5[:5] == "00000":
		print str(i) + " " + md5 + " " + "".join(password) + " " + md5[6]
		if ord(md5[5]) < 56:
			if password[int(md5[5])] == " ":
				password[int(md5[5])] = md5[6]
	i += 1
print "".join(password)
