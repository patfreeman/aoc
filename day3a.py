#!/usr/bin/env python
fp = open('input3.txt', 'r')
cnt = 0

for line in fp.readlines():
	sides = sorted(map(int,line.strip().split()), reverse=True)
	if sides[0] <= sides[1] + sides[2]:
		cnt+=1
	print " ".join(map(str,sides)) + " " + str(cnt)
print cnt
