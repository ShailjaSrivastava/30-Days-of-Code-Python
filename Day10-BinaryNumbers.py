#!/bin/python3

import math
import os
import random
import re
import sys


def find_max_ones(number):
    maxLength = 0

    while number > 0:
        left_shifted_number = number << 1
        number = number & left_shifted_number
        maxLength += 1

    return maxLength
    
if __name__ == '__main__':
    n = int(input().strip())
    c=find_max_ones(n)
    print(c)
