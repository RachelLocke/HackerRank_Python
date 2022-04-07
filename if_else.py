#!/bin/python3
# ===================================================================================================
# Author: Rachel Locke
# Date: April 6, 2022
# ---------------------------------------------------------------------------------------------------
# Project: If-Else by Hacker Rank
# Task:
#   Given an integer, , perform the following conditional actions:

#   If  is odd, print Weird
#   If  is even and in the inclusive range of  to , print Not Weird
#   If  is even and in the inclusive range of  to , print Weird
#   If  is even and greater than , print Not Weird

# Input Format:
# A single line containing a positive integer, .

# Constraints:
# 1 <= n <= 100

# Output Format:
# Print Weird if the number is weird. Otherwise, print Not Weird.
# ===================================================================================================

# Retrieve imports
import math
import os
import random
import re
import sys

def main():
    # Prompt the user to enter a number to evaluate.
    n = int(input("Enter a number:").strip())
    
    if(n%2 != 0): # The number is odd...
        print("Weird")
    elif(n % 2 == 0): # The number is even...
        if(2 <= n <= 5):
            print("Not Weird")
        elif(6 <= n <= 20):
            print("Weird")
        elif(n > 20):
            print("Not Weird")
            
if __name__ == '__main__':
    main()