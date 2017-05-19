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

for line in fp.readlines():
	sides = sorted(map(int,line.strip().split()), reverse=True)
	if sides[0] <= sides[1] + sides[2]:
		cnt+=1
	if args.verbose:
		print " ".join(map(str,sides)) + " " + str(cnt)
print cnt
fp.close()
