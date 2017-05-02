#!/usr/bin/env python
import re
import string

def chksum(data):
	ret = ""
	occurance_dict = {}
	chars = dict((el,0) for el in string.lowercase[:26])
	tops = 5

	for char in data:
		chars[char] += 1
	for key, value in sorted(chars.iteritems(), key=lambda (k,v): (v,k), reverse=True):
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
		if tops == 0:
			break
		for letter in sorted(occurance_dict[key]['keys']):
			ret = ret + letter
			tops -= 1
			if tops == 0:
				break
	return ret

fp = open('input4.txt', 'r')
for line in fp.readlines():
	data = re.match(r'^([a-z\-]*)-(\d+)\[(\w{5})\]\n',line)
	if data.group(3) == chksum(re.sub(r'-', r'', data.group(1))):
		room_name = ''
		for char in data.group(1):
			if char == '-':
				room_name = room_name + ' '
			else:
				room_name = room_name + chr( ((ord(char)-97) + int(data.group(2))) % 26 + 97 )
		if re.match('north.*pole', room_name):
			print room_name + " is in sector " + data.group(2)
