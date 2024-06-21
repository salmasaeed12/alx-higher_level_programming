#!/usr/bin/python3
import sys
a = len(sys.argv)
if a == 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(a-1))
    for i in range(1, a):
        print("{}: {}".format(i, sys.argv[i]))
