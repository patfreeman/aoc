#!/usr/bin/env python
import re
import sys

input = ""
fp = open('input1.txt', 'r')
for line in fp.readlines():
	input += line
current_direction = 1
ew = 0
ns = 0
history = [(0,0)]

def check_history(current):
	for tup in history:
		if tup == current:
			print "We found a location we have been"
			total_dist = abs(current[0]) + abs(current[1])
			print total_dist
			sys.exit(0)
	

def append_history(north, east):
	print history
	current_coords = []
	current_coords.append(history[len(history)-1][0])
	current_coords.append(history[len(history)-1][1])
	print current_coords
	while north > 0:
		current_coords[0] += 1
		check_history((current_coords[0],current_coords[1]))
		history.append((current_coords[0],current_coords[1]))
		north -= 1
	while north < 0:
		current_coords[0] -= 1
		check_history((current_coords[0],current_coords[1]))
		history.append((current_coords[0],current_coords[1]))
		north += 1
	while east > 0:
		current_coords[1] += 1
		check_history((current_coords[0],current_coords[1]))
		history.append((current_coords[0],current_coords[1]))
		east -= 1
	while east < 0:
		current_coords[1] -= 1
		check_history((current_coords[0],current_coords[1]))
		history.append((current_coords[0],current_coords[1]))
		east += 1

for direction in input.split(', '):
	match = re.search(r"(\w)(\d+)", direction);
	turn = 0
	if match:
		if match.group(1) == "L":
			turn = 1
		elif match.group(1) == "R":
			turn = 2
		else:
			print direction
			continue
		print direction
		print current_direction
		if current_direction == 1: # North
			if turn == 1:
				ew -= int(match.group(2))
				current_direction = 4
				append_history(0,0 - int(match.group(2)))
			else:
				ew += int(match.group(2))
				current_direction = 2
				append_history(0,int(match.group(2)))
		elif current_direction == 2: # East
			if turn == 2:
				ns -= int(match.group(2))
				current_direction = 3
				append_history(0 - int(match.group(2)),0)
			else:
				ns += int(match.group(2))
				current_direction = 1
				append_history(int(match.group(2)),0)
		elif current_direction == 3: # South
			if turn == 2:
				ew -= int(match.group(2))
				current_direction = 4
				append_history(0,0 - int(match.group(2)))
			else:
				ew += int(match.group(2))
				current_direction = 2
				append_history(0,int(match.group(2)))
		elif current_direction == 4: # West
			if turn == 1:
				ns -= int(match.group(2))
				current_direction = 3
				append_history(0 - int(match.group(2)),0)
			else:
				ns += int(match.group(2))
				current_direction = 1
				append_history(int(match.group(2)),0)
	else:
		print "failed to match"
		print direction
	print "Go " + str(ns) + " blocks north"
	print "Go " + str(ew) + " blocks east"
total_dist = abs(ns) + abs(ew)
print total_dist
fp.close()
