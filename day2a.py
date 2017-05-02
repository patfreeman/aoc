#!/usr/bin/env python
import sys

keypad = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

fp = open('input2.txt', 'r')
for line in fp.readlines():
	x = 0
	y = 0
	location = "5"
	for dir in line:
		if dir == "L":
			x -= 1
		if dir == "R":
			x += 1
		if dir == "U":
			y -= 1
		if dir == "D":
			y += 1
		if x < 0:
			x = -1
		if x > 0:
			x = 1
		if y < 0:
			y = -1
		if y > 0:
			y = 1
	sys.stdout.write(str(keypad[y+1][x+1]))
	sys.stdout.flush()
print ""
sys.exit(0)
