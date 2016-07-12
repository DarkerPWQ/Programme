# -*- coding: utf-8 -*-
import time
import datetime
#num = raw_input("please input a num")
start_time = time.time()
#num = int(num)
def isPrime(num):
    if num<2:
        return False
    else:
        for i in range(2,num):
            if i*i<=num:
                if num%i==0:
                    return False
            else:
                break
        return True            
#print isPrime(num)
#time.sleep(2)
end_time = time.time()
print type(end_time)
run_time = end_time-start_time
print type(run_time)
print "run time is " ,run_time
day_time=datetime.datetime.now()
yes_time=datetime.timedelta(days=1)
q=str(datetime.datetime.now())[0:10]
print q
nowtime = datetime.datetime.strptime(q, "%Y-%m-%d")
print nowtime
nowtime_char=str(nowtime)[0:10]#当前时间的字符串
