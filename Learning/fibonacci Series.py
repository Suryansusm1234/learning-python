def fib (num):
    if num == 1 or num == 0 :
        return 1
    else:
        return fib(num-1)+ fib(num -2)
a = int(input("Enter A number:-"))
print(fib(a))