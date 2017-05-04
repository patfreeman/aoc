#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Finds The number of valid triangles')
parser.add_argument('input_file', metavar='<inputfile>', type=str, default='input3.txt', nargs = '?',
		help='the name of the input file. defaults to input3.txt')
parser.add_argument('-v', '--verbose', action='store_true',
		help='enable verbose output')
args = parser.parse_args()

fp = open(args.input_file, 'r')

cnt = 0
def test(sides):
	if sides[0] < sides[1] + sides[2]:
		return True

line1 = fp.readline()
while line1:
	line2 = fp.readline()
	line3 = fp.readline()
	side1 = line1.strip().split()
	side2 = line2.strip().split()
	side3 = line3.strip().split()
	for index in range(0,len(side1)):
		if test(sorted(map(int,(side1[index], side2[index], side3[index])), reverse=True)):
			cnt+=1
		if args.verbose:
			print side1[index] + " " + side2[index] + " " + side3[index] + " " + str(cnt)
	line1 = fp.readline();
print cnt
fp.close()
