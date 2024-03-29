#!/usr/bin/env python

import secret_number
n = 1000

def play():
    i = 0
    high = 1000
    low = 0
    while i < 10:
        x = BinarySearch(low, high)
        s = secret_number.guess(x)
        if s == 'too-low':
            low = x
        elif s == 'too-high':
            high = x
        i += 1

def BinarySearch(first, last):
    midpoint = (first + last) // 2
    return midpoint
