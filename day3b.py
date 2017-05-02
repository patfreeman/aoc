#!/usr/bin/env python
import re
import sys

fp = open('input3.txt', 'r')

cnt = 0
def test(side1, side2, side3):
	if int(side1) < int(side2) + int(side3) and int(side2) < int(side1) + int(side3) and int(side3) < int(side1) + int(side2):
		return True

line1 = fp.readline()
while line1:
	line2 = fp.readline();
	line3 = fp.readline();
	side1 = re.split('\s+', line1.strip())
	side2 = re.split('\s+', line2.strip())
	side3 = re.split('\s+', line3.strip())
	for index in range(0,len(side1)):
		if test(side1[index], side2[index], side3[index]):
			cnt+=1
		print side1[index] + " " + side2[index] + " " + side3[index] + " " + str(cnt)
	line1 = fp.readline();
print cnt
