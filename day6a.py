#!/usr/bin/env python
import re
import string
import sys

def 

chars = []
occurance_dict = {}
fp = open('input6.txt', 'r')
for line in fp.readlines():
	idx = 0
	for char in line.strip():
		try:
			chars[idx]
		except:
			chars.append(dict((el,0) for el in string.lowercase[:26]))
		chars[idx][char] += 1
		idx += 1
print chars

for idx in chars:
	print "Position " + str(idx)
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
	
	for key in sorted(occurance_dict.keys(), reverse=True):
		for letter in sorted(occurance_dict[key]['keys']):
			sys.stdout.write(letter)
			break
