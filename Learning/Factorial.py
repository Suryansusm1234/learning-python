a =int(input("Enter a Number whose Factorial is to be calculated:-"))
def fact(num):
    if num == 0 or num==1:
        return 1
    else:
        return num * fact(num-1)
print(f"The factorial of the given number is {fact(a)}")