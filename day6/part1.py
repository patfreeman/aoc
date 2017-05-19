#!/usr/bin/env python
import argparse
import string
import sys

parser = argparse.ArgumentParser(description='Finds the error-crrected message')
parser.add_argument('input_file', metavar='<inputfile>', type=str, default='input6.txt', nargs = '?',
		help='the name of the input file. defaults to input6.txt')
parser.add_argument('-v', '--verbose', action='store_true',
		help='enable verbose output')
args = parser.parse_args()

def top_char(odict):
	for key in sorted(odict.keys(), reverse=True):
		for letter in sorted(odict[key]['keys']):
			return letter
			
chars = []
fp = open(args.input_file, 'r')
for line in fp.readlines():
	idx = 0
	if args.verbose:
		print "Reading line " + line.strip()
	for char in line.strip():
		try:
			chars[idx]
		except:
			chars.append(dict((el,0) for el in string.lowercase[:26]))
		if args.verbose:
			print "Adding to chars[" + str(idx) + "][" + char + "]"
		chars[idx][char] += 1
		idx += 1
	if args.verbose:
		print chars

for idx in chars:
	occurance_dict = {}
	for key, value in sorted(idx.iteritems(), key=lambda (k,v): (v,k)):
		try:
			occurance_dict[value]
		except:
			occurance_dict[value] = {}
		try:
			occurance_dict[value]['value']
		except:
			occurance_dict[value]['value'] = value
			occurance_dict[value]['keys'] = []
		if value == occurance_dict[value]['value']:
			occurance_dict[value]['keys'].append(key)
	sys.stdout.write(top_char(occurance_dict))
print
