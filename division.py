#!/bin/python3
# ===================================================================================================
# Author: Rachel Locke
# Date: April 6, 2022
# ---------------------------------------------------------------------------------------------------
# Project: If-Else by Hacker Rank
# Task:
#   The provided code stub reads two integers, a and b , from STDIN.
#
#   Add logic to print two lines. The first line should contain the result of integer division,  
#   a//b . The second line should contain the result of float division, a/b .
#
#   No rounding or formatting is necessary.
# ===================================================================================================

def main():
    a = int(input("Enter integer for 'a': "))
    b = int(input("Enter integer for 'b': "))
    
    int_div = a//b
    float_div = a/b
    
    print(int_div)
    print(float_div)

if __name__ == '__main__':
    main()