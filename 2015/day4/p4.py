#!/usr/bin/python
import hashlib
import sys

v = sys.argv[1]
suffix = ""
i = 0
while True:
    h = hashlib.md5(v + suffix).hexdigest()
    if h.startswith("00000"):
        break
    i += 1
    suffix = str(i)
print(h)
print(suffix)
