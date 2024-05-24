#!/usr/bin/env python3

import sys

args = sys.argv

if len(args) != 3:
    print("Usage: " + args[0] + " name age")
    sys.exit()

name = args[1]
age = args[2]

print("Hi " + name + ", you are " + str(age) + " years old.")