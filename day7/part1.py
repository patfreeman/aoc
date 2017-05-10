#!/usr/bin/env python
import argparse
import re
import string
import sys

parser = argparse.ArgumentParser(description='IPv7: How many IPs support TLS?')
parser.add_argument('input_file', metavar='<inputfile>', type=str, default='input7.txt', nargs = '?',
		help='the name of the input file. defaults to input7.txt')
parser.add_argument('-v', '--verbose', action='store_true',
		help='enable verbose output')
args = parser.parse_args()

ABBALENGTH = 4

def abba(data):
	half=len(data)/2
	lhs = data[:half]
	rhs = data[half:]
	reversedrhs = rhs[::-1]
	print "Testing " + lhs + " == " + reversedrhs
	if lhs == reversedrhs and lhs != rhs:
		return True
	else:
		return False

def tls(data):
	for ind in range(1, len(data), 2):
		if args.verbose:
			print "Stepping through bracketed data " + data[ind] + " looking for ABBAs"
		for abbaindex in range(0, len(data[ind]) - ABBALENGTH + 1):
			if abba(data[ind][abbaindex:abbaindex+ABBALENGTH]):
				return False
	for ind in range(0, len(data), 2):
		if args.verbose:
			print "Stepping through unbracketed data " + data[ind] + " looking for ABBAs"
		for abbaindex in range(0, len(data[ind]) - ABBALENGTH + 1):
			if abba(data[ind][abbaindex:abbaindex+ABBALENGTH]):
				return True

count = 0
fp = open(args.input_file, 'r')
for line in fp.readlines():
	if args.verbose:
		print "Reading line " + line.strip()
	data = re.split('\W',line.strip())
	if tls(data):
		if args.verbose:
			print "Line " + line.strip() + " supports TLS"
		count += 1
	else:
		if args.verbose:
			print "Line " + line.strip() + " does not support TLS"
print str(count)
