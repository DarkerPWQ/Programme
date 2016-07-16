__author__ = 'pwq'
# -*- coding: utf-8 -*-
class Insertsort(object):
    def __init__(self,array):
        self.array = array
        self.N = len(self.array)
    def less(self,i,j):
        if self.array[i]<=self.array[j]:
            return True
        else:
            return False
    def exch(self,i,j):
        temp = self.array[j]
        self.array[j] = self.array[i]
        self.array[i] = temp
    def show(self):
        for item in self.array:
            print item,
    def sort(self):
        for i in range(1,self.N):
            for j in range(i,0,-1):
                if self.less(j,j-1):
                    self.exch(j,j-1)
a=[1,23,4,5,6,7,2,54,3,4,56,6,7,8,9,44,32,1,1,231,231]
sort_A = Insertsort(a)
sort_A.sort()
sort_A.show()



