num = int(input("Enter a number:-"))
sum = 0
def digit_sum(a):
    global sum
    if a == 0:
        return 0
    else:
        sum += a%10
        return digit_sum(a/10)
digit_sum(num)
print(f"The sum of the digit is {int(sum)}")