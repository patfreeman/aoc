#!/usr/bin/env python
import argparse
import sys

parser = argparse.ArgumentParser(description='Finds the bathroom code')
parser.add_argument('input_file', metavar='<inputfile>', type=str, default='input2.txt', nargs = '?',
		help='the name of the input file. defaults to input2.txt')
parser.add_argument('-v', '--verbose', action='store_true',
		help='enable verbose output')
args = parser.parse_args()

code = ""
keypad = [ [0, 0, '1', 0, 0],
	[0, '2', '3', '4', 0],
	['5', '6', '7', '8', '9'],
	[0, 'A', 'B', 'C', 0],
	[0, 0, 'D', 0, 0] ]

fp = open(args.input_file, 'r')

if args.verbose:
	print "using keypad:"
	for line in keypad:
		print line

for line in fp.readlines():
	x = 0
	y = 2
	if args.verbose:
		print "Starting at location " + str(keypad[y][x]) + ", coordinates [" + str(x) + "," + str(y) + "]"
	for dir in line.strip():
		if dir == "L":
			if x-1 >= 0 and keypad[y][x-1] != 0:
				x -= 1
		elif dir == "R":
			if x+1 <= 4 and keypad[y][x+1] != 0:
				x += 1
		elif dir == "U":
			if y-1 >= 0 and keypad[y-1][x] != 0:
				y -= 1
		elif dir == "D":
			if y+1 <= 4 and keypad[y+1][x] != 0:
				y += 1
		else:
			print "Skipping unknown direction \"" + dir + "\""
			continue
		if args.verbose:
			print "Moving " + dir + " to location " + str(keypad[y][x]) + ", coordinates [" + str(x) + "," + str(y) + "]"
	code = code + str(keypad[y][x])
print code
