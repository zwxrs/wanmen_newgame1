# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:41:44 2018

@author: zwxrs
"""

from const import PI

def calc_round_area(radius):
    return PI * (radius ** 2)

def main():
    print("round area: ", calc_round_area(2))

main()