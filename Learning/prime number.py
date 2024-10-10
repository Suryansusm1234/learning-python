import math
prime = True
a = int(input("Enter a number:-"))
for i in range(2,int(math.sqrt(a))+1):
    if a%i==0:
        prime = False
        break
if prime:
    print("The number is prime")
else:
    print("The number is not prime")