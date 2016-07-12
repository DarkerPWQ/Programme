# -*- coding: utf-8 -*-
import time 
a = [2,3,4,52,1,3,5,6,8,9,7,67,6,4,43,3,2,2,342,4,4,4,2,22,2,4,6,67,7]
class choose_sort:
    def __init__(self,list_sort):
        self.list_sort = list_sort
        self.len = len(self.list_sort)
    def less(self,i,j):
        if self.list_sort[i]<self.list_sort[j]:
            return True
        return False
    def exch(self,i,j):
        temp = self.list_sort[j]
        self.list_sort[j] = self.list_sort[i]
        self.list_sort[i] = temp
    def show(self):
        for i in range(self.len):
            print self.list_sort[i],
    
    def sort1(self):
        for i in range(self.len):
            min = i
            for j in range(i+1,self.len):
                if self.less(j,i):
                    self.exch(i,j)
                    
            
        
    def sort(self):
        for i in range(self.len):
            min = i
            for j in range(i+1,self.len):
                if self.less(j,min):
                    min =j
            self.exch(i,min)

    def sortmain(self):
        self.sort();
        self.show();
sort = choose_sort(a)
start_time = time.time()

sort.sortmain()
end_time = time.time()
print end_time-start_time
