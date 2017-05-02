#!/usr/bin/env python
import re
import sys

fp = open('input3.txt', 'r')

cnt = 0

for line in fp.readlines():
	sides = re.split('\s+', line.strip())
	if int(sides[0]) < int(sides[1]) + int(sides[2]) and int(sides[1]) < int(sides[0]) + int(sides[2]) and int(sides[2]) < int(sides[0]) + int(sides[1]):
		cnt+=1
	print sides[0] + " " + sides[1] + " " + sides[2] + " " + str(cnt)
print cnt
