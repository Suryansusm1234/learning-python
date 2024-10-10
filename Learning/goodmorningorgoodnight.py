import time
t = int(time.strftime('%H'))
if (t >=0 and t<12):
    print("Good Moring Sir")
elif(t>=12 and t <=15):
    print("Good After Noon Sir")
elif(t >=15 and t <= 20 ):
    print("Good Evening Sir")
else:
    print("Good night Sir")
    