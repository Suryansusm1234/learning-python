num1 = int(input("Enter the 1st number:-"))
num2 = int(input("Enter the 2nd number:-"))
def gcd(a,b):
    while(b !=0):
        a,b =b,a%b
    return a
c=gcd(num1,num2)
print(f"The G.C.D of two number is:-{c}")
    