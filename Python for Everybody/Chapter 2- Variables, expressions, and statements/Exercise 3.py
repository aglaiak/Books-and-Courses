# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:01:28 2023

@author: Aglaia
"""

hours = input("Enter total amount of working hours")
rate= input("Enter rate per hour")

#need to convert the input to an integer because the built-in function "input" returns what the user typed as a string.

pay= int(hours)*int(rate)
print(pay)