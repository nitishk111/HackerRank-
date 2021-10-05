#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def Gregorian_leap(year):
    if year%400==0:
        return True
    if year%4==0 and year%100!=0:
        return True

def Julian_leap(year):
    if year%4==0:
        return True
    
        
def dayOfProgrammer(year):
    if year>1917:
        if Gregorian_leap(year):
            return '12.09.'+str(year)
        return '13.09.'+str(year)
    elif year==1918:
            return '26.09.1918'
    else:
        if Julian_leap(year):
            return '12.09.'+str(year)
        return '13.09.'+str(year)
        
            

if __name__ == '__main__':


    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)


    fptr.close()
