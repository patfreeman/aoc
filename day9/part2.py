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
	ret = 0
	if args.verbose:
		print "calling decompress on line: " + line
	charpointer = 0
	while charpointer < len(line):
		char=line[charpointer]
       		if args.verbose:
               		print "Testing char \"" + char + "\" at position " + str(charpointer)
		if char == '(':
			data = re.match('^\((\d+)x(\d+)\)(.*)', line[charpointer:])
			data2 = re.match('^\((\d+)x(\d+)\)(.{' + data.group(1) + '})', line[charpointer:])
			if args.verbose:
				print "Found expansion"
				print data2.group(1)
				print data2.group(2)
				print data2.group(3)
				#print data.groups()
			# Skip over the length of the compression and the control chars
			charpointer += len("".join(data2.groups())) + 3
			# Add the decompressed length of the inner compression
			ret += decompress(data2.group(3)) * int(data2.group(2))
			if args.verbose:
				print "adding " + data2.group(2) + " * " + str(len(data2.group(3)))
		elif re.search('(\s|\n)', char):
			charpointer += 1
			continue
		else:
			charpointer += 1
			ret += 1
	if args.verbose:
		print "returning ret " + str(ret)
	return ret

fp = open(args.input_file, 'r')
for line in fp.readlines():
	print decompress(line)
