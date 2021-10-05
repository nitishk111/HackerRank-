# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 22:41:59 2020

@author: Nitish
"""


# Taking word as input.

s=input("Enter a word:: ")

for i in range(len(s)-1,-1,-1):
    print(s[i],end="")