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

def aba(data):
	if args.verbose:
		print "Testing " + data
	if data[0] == data[2] and data[0] != data[1]:
		return True
	else:
		return False

def ssl(data):
	for ind in range(0, len(data), 2):
		if args.verbose:
			print "Stepping through unbracketed data " + data[ind] + " looking for ABAs"
		for abaindex in range(0, len(data[ind]) - 2):
			if aba(data[ind][abaindex:abaindex+3]):
				bab=data[ind][abaindex+1] + data[ind][abaindex] + data[ind][abaindex+1]
				for babind in range(1, len(data), 2):
					if args.verbose:
						print "Stepping through bracketed data " + data[babind] + " looking for BAB " + bab
					for babindex in range(0, len(data[babind]) - 2):
						if data[babind][babindex:babindex+3] == bab:
							return True

count = 0
fp = open(args.input_file, 'r')
for line in fp.readlines():
	if args.verbose:
		print "Reading line " + line.strip()
	data = re.split('\W',line.strip())
	if ssl(data):
		if args.verbose:
			print "Line " + line.strip() + " supports SSL"
		count += 1
	else:
		if args.verbose:
			print "Line " + line.strip() + " does not support SSL"
print str(count)
