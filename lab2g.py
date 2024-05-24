#!/usr/bin/env python3

# Author: Derrek Russell
# AuthorID: drussell6
# Date Created: 2024/05/23

import sys

args = sys.argv

if len(args) > 1:
    timer = int(args[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer -= 1

print("blast off!")
