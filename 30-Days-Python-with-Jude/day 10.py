import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

bn = "{0:b}".format(n)
print(len(list(max(bn.split("0")))))

#God in heaven knows i dont understand this code