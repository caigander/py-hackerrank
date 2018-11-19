#!/bin/python3

import math
import os
import random
import re
import sys

def weird(a):
    if a % 2 >= 1: 
        print('Weird')
    if a % 2 == 0 and a >= 2 and a <= 5: 
        print('Not Weird')        
    if a % 2 == 0 and a >= 6 and a <= 20: 
        print('Weird')
    if a % 2 == 0 and a >= 20: 
        print('Not Weird')

if __name__ == '__main__':
    N = int(input())
    weird(N)
