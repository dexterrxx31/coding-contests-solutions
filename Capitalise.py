#!/bin/python3

import math
import os
import random
import re
import sys
import os 

def solve(s):
    if s[0].isnumeric():
        pass
    else:
        s = s[0].capitalize() + s[1:]
               
    for x in range(len(s)) :
        if x > 0 and s[x-1] == " ":
            s = s[:x] + s[x].capitalize() + s[x+1:]
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
