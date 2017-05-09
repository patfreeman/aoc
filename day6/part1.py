#!/usr/bin/env python
import string
import sys


chars = []
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

def top_char(odict):
	for key in sorted(odict.keys(), reverse=True):
		for letter in sorted(odict[key]['keys']):
			return letter
			

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
