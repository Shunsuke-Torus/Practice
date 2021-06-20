# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 21:40:44 2021

@author: shun
"""
import math
import sympy

p =int(input("p-1="))
q =int(input("q-1="))
e =int(input("e="))
n = p*q
GCD = math.gcd(p,q)
L = int(n/GCD)#秘密
print("最小公倍数:",L)

print("ed+Ly=1")
x,y,t = sympy.gcdex(e,L)
d = x
print("復号化鍵製作完了d:",d)