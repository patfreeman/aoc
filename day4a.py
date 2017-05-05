#!/usr/bin/env python
import argparse
import re
import string

parser = argparse.ArgumentParser(description='Finds the number of valid rooms')
parser.add_argument('input_file', metavar='<inputfile>', type=str, default='input4.txt', nargs = '?',
                help='the name of the input file. defaults to input4.txt')
parser.add_argument('-v', '--verbose', action='store_true',
                help='enable verbose output')
args = parser.parse_args()

def chksum(data):
	ret = ""
	occurance_dict = {}
	chars = dict((el,0) for el in string.lowercase[:26])
	tops = 5

	for char in data:
		chars[char] += 1
	for key, value in sorted(chars.iteritems(), key=lambda (k,v): (v,k)):
		try:
			occurance_dict[value]
		except:
			occurance_dict[value] = []
		occurance_dict[value].append(key)
	if args.verbose:
		print occurance_dict
	for key in sorted(occurance_dict.keys(), reverse=True):
		if tops == 0:
			break
		for letter in sorted(occurance_dict[key]):
			ret = ret + letter
			tops -= 1
			if tops == 0:
				return ret

total = 0
fp = open(args.input_file, 'r')
for line in fp.readlines():
	if args.verbose:
		print "Checking line " + line.strip()
	data = re.match(r'^([a-z\-]*)-(\d+)\[(\w{5})\]\n',line)
	checksum = chksum(re.sub(r'-', r'', data.group(1)))
	if data.group(3) == checksum:
		total += int(data.group(2))
		if args.verbose:
			print "Calculated chksums match: " + checksum
			print "Added sector " + data.group(2) + " to total " + str(total)
	else:
		if args.verbose:
			print "Calculated chksums mismatch: " + data.group(3) + " != " + checksum
print str(total)
fp.close()
