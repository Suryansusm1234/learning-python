n =int(input("Enter the Range upto which you want to calculate the fibonacci Series:-"))
for i in range(n):
    def fib (num):
        if num == 1 or num == 0 :
            return 1
        else:
            return fib(num-1)+ fib(num -2)
    print(fib(i) ,end=(","))