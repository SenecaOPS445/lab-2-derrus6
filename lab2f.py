#!/usr/bin/env python3

# Author: Derrek Russell
# AuthorID: drussell6
# Date Created: 2024/05/23

import sys

args = sys.argv

timer = int(args[1])

while timer != 0:
    print(timer)
    timer -= 1

print("blast off!")
