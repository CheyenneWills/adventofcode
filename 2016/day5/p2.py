#!/usr/bin/python
import hashlib
import sys

v = sys.argv[1]
index = 0
pw = list(8*'.')
found = 0
i = 0
while True:
    suffix = str(i)
    h = hashlib.md5(v+suffix).hexdigest()
    if h.startswith("00000"):
    	pos = h[5]
    	c = h[6]
    	if pos >= '0' and pos <= '7':
    		pos = int(pos)
    		if pw[pos] == '.':

    			pw[pos] = c
    			found += 1
    			if found == 8:
    				break

        	print(v+suffix,h,pw)

    i += 1

print(''.join(pw))

