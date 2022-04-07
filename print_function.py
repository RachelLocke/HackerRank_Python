#!/bin/python3
# ===================================================================================================
# Author: Rachel Locke
# Date: April 6, 2022
# ---------------------------------------------------------------------------------------------------
# Project: Print Function by Hacker Rank
# Task:
#   the included code stub will read an integer, nan, from STDIN. Without using any string methods, 
#   try to print the following:   123...n
#   Note that "..." represents the consecutive values in between.
#
# Input Format
#   the first line contains an integer n.
#
# Constraints
#   1 <= n <= 150
#
# Output Format
#   Print the list of integers from 1 through n as a string, without spaces.
# ===================================================================================================

def main():
    n = int(input("Enter an integer: "))
    for i in range(1,n + 1):
        print(i, end='')

if __name__ == '__main__':
    main()