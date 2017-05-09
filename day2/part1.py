#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Finds the bathroom code')
parser.add_argument('input_file', metavar='<inputfile>', type=str, default='input2.txt', nargs = '?',
		help='the name of the input file. defaults to input2.txt')
parser.add_argument('-v', '--verbose', action='store_true',
		help='enable verbose output')
args = parser.parse_args()

code = ""
keypad = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
fp = open(args.input_file, 'r')

if args.verbose:
	print "using keypad:"
	for line in keypad:
		print line

for line in fp.readlines():
	x = 0
	y = 0
	if args.verbose:
		print "Starting at location " + str(keypad[y+1][x+1]) + ", coordinates [" + str(x) + "," + str(y) + "]"
	for dir in line.strip():
		if dir == "L":
			x -= 1
		elif dir == "R":
			x += 1
		elif dir == "U":
			y -= 1
		elif dir == "D":
			y += 1
		else:
			print "Skipping unknown direction \"" + dir + "\""
			continue
		if x < 0:
			x = -1
		if x > 0:
			x = 1
		if y < 0:
			y = -1
		if y > 0:
			y = 1
		if args.verbose:
			print "Moving " + dir + " to location " + str(keypad[y+1][x+1]) + ", coordinates [" + str(x) + "," + str(y) + "]"
	code = code + str(keypad[y+1][x+1])
print code
fp.close()
