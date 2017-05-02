#!/usr/bin/env python
import sys


keypad = [ [0, 0, '1', 0, 0],
	[0, '2', '3', '4', 0],
	['5', '6', '7', '8', '9'],
	[0, 'A', 'B', 'C', 0],
	[0, 0, 'D', 0, 0] ]

fp = open('input2.txt', 'r')
for line in fp.readlines():
	x = 0
	y = 2
	location = "5"
	for dir in line:
		if dir == "L":
			if x-1 >= 0 and keypad[y][x-1] != 0:
				x -= 1
		if dir == "R":
			if x+1 <= 4 and keypad[y][x+1] != 0:
				x += 1
		if dir == "U":
			if y-1 >= 0 and keypad[y-1][x] != 0:
				y -= 1
		if dir == "D":
			if y+1 <= 4 and keypad[y+1][x] != 0:
				y += 1
	sys.stdout.write(str(keypad[y][x]))
	sys.stdout.flush()
print ""
sys.exit(0)
