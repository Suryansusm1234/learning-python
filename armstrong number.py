#To print all the armstrong number from 1 to 10000
import math
count : int  
r :str
for i  in range(1,10001):
      sum = 0
      r= str(i)
      count = len(r)
      a = int(i)
      while(i !=0):
        b= i%10
        sum += math.pow(b,count)
        i = i //10
      if(sum == a):
        print(a,end=(','))