import math
a = int(input("Enter the p :-"))
b = int (input("Enter the b :-"))
c = int(input("Enter the h:-"))
d = max(a,b,c)
if(d!=c):
    print("Invalid inputs")
else:
    if(pow(d,2)==(pow(a,2)+pow(b,2))):
        print("This are pythogorus triplets")
    else:
        print("This are not pythogorus triplets")

