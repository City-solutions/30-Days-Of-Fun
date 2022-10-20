#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
if (N%2 == 1):
    print('Weird')

range1= range(2,6)
if N in range1 and (N%2 == 0):
  print('Not Weird')

range2= range(6, 21)
if N in range2 and (N%2 == 0):
  print('Weird')

if (N > 20) and (N%2 == 0):
    print('Not Weird')
