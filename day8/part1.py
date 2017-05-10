#!/usr/bin/env python
import argparse
import re
import sys
import time

parser = argparse.ArgumentParser(description='IPv7: How many IPs support TLS?')
parser.add_argument('input_file', metavar='<inputfile>', type=str, default='input8.txt', nargs = '?',
		help='the name of the input file. defaults to input8.txt')
parser.add_argument('-v', '--verbose', action='store_true',
		help='enable verbose output')
args = parser.parse_args()

screen = [ [0 for x in range(50)] for y in range(6) ]


def rect (a, b):
	if args.verbose:
		print "setting 0,0 through " + str(a) + "," + str(b) + " to on"
	for x in range(0,a):
		for y in range(0,b):
			screen[y][x]=1
	if args.verbose:
		print screen
	return

def rotaterow (row, offset):
	moddedoffset = (len(screen[row])-offset)%len(screen[row])
	temp = screen[row][moddedoffset:] + screen[row][:moddedoffset]
	if args.verbose:
		print "Setting row to " + ",".join(map(str,temp))
	screen[row]=temp
	return

def rotatecol (col, offset):
	temp = []
	for row in range(0,len(screen)):
		temp.append(screen[(row-offset)%len(screen)][col])
	if args.verbose:
		print "Setting column " + str(col) + " to "  + ",".join(map(str,temp))
	for row in range(0,len(screen)):
		screen[row][col]=temp[row]
	return

def printscreen ():
	count = 0
	time.sleep(0.05)
	sys.stdout.write("\x1b[2J\x1b[H")
	for x in screen:
		for y in x:
			count += y
			if y:
				sys.stdout.write("*")
			else:
				sys.stdout.write(" ")
		sys.stdout.write("\n")
	sys.stdout.flush()
	print count
	return

fp = open(args.input_file, 'r')
for line in fp.readlines():
        if args.verbose:
                print "Reading line " + line.strip()
	if "rect" in line:
		data = re.match(r'^rect (\d+)x(\d+)',line.strip())
		rect(int(data.group(1)), int(data.group(2)))
	elif "row" in line:
		data = re.match(r'^rotate row y=(\d+) by (\d+)',line.strip())
		rotaterow(int(data.group(1)), int(data.group(2)))
	elif "column" in line:
		data = re.match(r'^rotate column x=(\d+) by (\d+)',line.strip())
		rotatecol(int(data.group(1)), int(data.group(2)))
	printscreen()
