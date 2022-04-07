#!/bin/python3
# ===================================================================================================
# Author: Rachel Locke
# Date: April 6, 2022
# ---------------------------------------------------------------------------------------------------
# Project: If-Else by Hacker Rank
# Task:
#   The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, 
#   print i^2.
# 
# Input Format
#   The first and only line contains the integer, n.
# 
# Constraints
#   1 <= n <= 20
#
# Output Format
#   Print n lines, one corresponding to each i.
# ===================================================================================================

def main():
    n = int(input())
    
    for i in range(n):
        print(i*i)

if __name__ == '__main__':
    main()