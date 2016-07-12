# -*- coding: utf-8 -*-
#斐波那契python实现：
def fbnx(n):
    if n<0:
        return False
    if n==0:
        return 0
    if n==1:
        return 1
    return fbnx(n-1)+fbnx(n-2)
print fbnx(3)
