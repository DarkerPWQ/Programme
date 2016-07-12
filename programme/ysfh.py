# -*- coding: utf-8 -*-
def ysfh(ysfh_list,n):
    if len(ysfh_list)==1:
        return ysfh_list
    next_ysfh_list = []
    for item in ysfh_list:
        n+=1
        if n!=3:
            next_ysfh_list.append(item)
        else:
            n=0
    return ysfh(next_ysfh_list,n)
ysfh_list = range(81)
print ysfh(ysfh_list,0)

