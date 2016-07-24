__author__ = 'pwq'
# -*- coding: utf-8 -*-
class BinarySearch(object):
    def __init__(self,Key):
        self.keys = Key;
        self.N = len(self.keys)
    def rank_recur(self,key,lo,hi):
        if lo>hi:return lo
        mid = lo+(hi-lo)/2
        if key>self.keys[mid]:
            return self.rank_recur(key,mid+1,hi)
        elif key<self.keys[mid]:
            return self.rank_recur(key,lo,mid-1)
        else:
            return mid
    def rank_itera(self,key):
        lo = 0
        hi = self.N-1
        while lo<=hi:
            mid = lo+(hi-lo)/2
            if key>self.keys[mid]:
                lo=mid+1
            elif key<self.keys[mid]:
                hi = mid-1
            else:
                return mid
    def rank(self,key):
        print self.rank_recur(key,0,self.N-1)

