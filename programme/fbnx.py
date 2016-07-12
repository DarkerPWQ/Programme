# -*- coding: utf-8 -*-
def fbnx(n):
    if n<0:
        return False
    if n==0:
        return 0
    if n==1:
        return 1
    return fbnx(n-1)+fbnx(n-2)
print fbnx(3)