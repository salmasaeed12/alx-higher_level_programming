#!/usr/bin/python3
import sys
i = len(sys.argv)
if i == 1:
    print("0 ")
else:
    m = 0
    for x in range(1, i):
        m += int(sys.argv[x])
    print("{} ".format(m))
