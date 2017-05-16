#!/usr/bin/env python
import argparse
import re

parser = argparse.ArgumentParser(description='decompression')
parser.add_argument('input_file', metavar='<inputfile>', type=str, default='input9.txt', nargs = '?',
		help='the name of the input file. defaults to input9.txt')
parser.add_argument('-v', '--verbose', action='store_true',
		help='enable verbose output')
args = parser.parse_args()


def decompress(line):
	charpointer = 0
	ret = ""
	while charpointer < len(line):
		char=line[charpointer]
        	if args.verbose:
                	print "Testing char \"" + char + "\" at position " + str(charpointer)
		if char == '(':
			data = re.match('^\((\d+)x(\d+)\)(.*)', line[charpointer:])
			if args.verbose:
				print "Found expansion"
				#print data.groups()
			for x in range(0,int(data.group(2))):
				addition = data.group(3)[0:int(data.group(1))]
				ret += addition
			charpointer += 3 + int(data.group(1)) + len(data.group(1)) + len(data.group(2))
		elif re.search('(\s|\n)', char):
			charpointer += 1
			continue
		else:
			ret += char
			charpointer += 1
	return ret

output = ""
fp = open(args.input_file, 'r')
for line in fp.readlines():
	output += decompress(line)
print output
print len(output)
