#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:40:55 2024

@author: student
"""

a=int(input("enter the 1st  no :"))
b=int(input("enter the 2nd  no :"))
c=int(input("enter the 3rd  no :"))
sum=a+b+c
product=a*b*c
average=sum/3
print("sum: ",sum)
print("product: ",product)
print("average: ",average)
print("largest no: ",max(a,b,c))
print("smallest no: ",min(a,b,c))