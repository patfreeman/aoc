#!/bin/bash
c=`head -1 input6.txt|wc -c`;for x in `seq 1 $((c - 1))`;do cat input6.txt|cut -c$x|sort|uniq -c|sort -n|head -1|awk '{ORS="";print $NF}';done;echo
