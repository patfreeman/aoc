#!/usr/bin/env python
import argparse
import re

parser = argparse.ArgumentParser(description='decompression')
parser.add_argument('input_file', metavar='<inputfile>', type=str, default='input10.txt', nargs = '?',
		help='the name of the input file. defaults to input10.txt')
parser.add_argument('-v', '--verbose', action='store_true',
		help='enable verbose output')
args = parser.parse_args()


bots = {}
fp = open(args.input_file, 'r')
for line in fp.readlines():
	#print "Parsing line " + line.strip()
	data = re.match('^value (\d+) goes to bot (\d+)', line)
	if data:
		try:
			bots[data.group(2)]['data']
		except:
			bots[data.group(2)]={}
			bots[data.group(2)]['data']=[]
			bots[data.group(2)]['instructions']={}
		try:
			bots[data.group(2)]['data'].append(data.group(1))
		except:
			bots[data.group(2)]['data']=[]
			bots[data.group(2)]['data'].append(data.group(1))
		print bots[data.group(2)]
	else:
		data = re.match('^bot (\d+) gives (\w+) to (\w+) (\d+) and (\w+) to (\w+) (\d+)', line)
		try:
			bots[data.group(1)]['instructions']
		except:
			bots[data.group(1)]={}
			bots[data.group(1)]['data']=[]
			bots[data.group(1)]['instructions']={}
		try:
			bots[data.group(1)]['instructions'][data.group(2)] = (data.group(3),data.group(4))
			bots[data.group(1)]['instructions'][data.group(5)] = (data.group(6),data.group(7))
		except:
			bots[data.group(1)]['instructions']={}
			bots[data.group(1)]['instructions'][data.group(2)] = (data.group(3),data.group(4))
			bots[data.group(1)]['instructions'][data.group(5)] = (data.group(6),data.group(7))
fp.close()

notfound = True
outputs = {}

while notfound:
	for bot in bots.keys():
		if len(bots[bot]['data']) == 2:
			hilow = sorted(map(int,bots[bot]['data']))
			for inst in bots[bot]['instructions']:
				dest = bots[bot]['instructions'][inst][0]
				number = bots[bot]['instructions'][inst][1]
				if inst == 'low':
					data = str(hilow[0])
				else:
					data = str(hilow[1])
				if dest == "output":
					print "Send " + data + " to output " + number
					try:
						outputs[number]
					except:
						outputs[number]=data
					try:
						if outputs['0'] and outputs['1'] and outputs['2']:
							print str( int(outputs['0']) * int(outputs['1']) * int(outputs['2']))
							notfound = False
					except:
						pass
				else:
					bots[number]['data'].append(data)
			bots[bot]['data']=[]
