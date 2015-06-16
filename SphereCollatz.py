#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """

    # pre-conditions & argument validity
    assert i > 0
    assert j > 0
    assert i < 1000000
    assert j < 1000000

    # makes sure that beginning of range is less than end
    # otherwise makes a switch    
    if j < i :
        temp = i;
        i = j;
        j = temp;

    # holds temporary maximum cycle length
    tempMax = 0;

    # iteration to find cycle length of range
    for pos in range(i, j+1) :
        cycle_length = collatz_cycle_length (pos)
        if cycle_length > tempMax :
            tempMax = cycle_length

    """
    # return-value validity
    assert tempMax > 0
    """

    return tempMax

# ------------
# collatz_cycle_length
# ------------

def collatz_cycle_length (l) :
    """
    l the integer to find cycle length of
    return the cycle length of the l
    """

    count = 1
    
    # pre-conditions
    assert l > 0
    assert l < 1000000

    # find cycle length using equation
    tempNum = l
    while tempNum > 1 : 
        if tempNum % 2 == 0 :
            tempNum /= 2
        else :
            tempNum = (3 * tempNum) + 1
        count += 1

    # post-conditions
    assert count > 0
    
    return count

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)



# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)

"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000
% RunCollatz.py < RunCollatz.in > RunCollatz.out
% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1
% pydoc3 -w Collatz
# That creates the file Collatz.html
"""
