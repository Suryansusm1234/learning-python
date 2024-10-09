a = int(input("Enter a number :-"))
sum = 0
sum2 = 0
while(a !=0):
    num = a%10
    sum2 += num 
    a = a//10
    sum = (sum *10) + num
print("The reversed form is:-",sum)
print("The sum of all the digits of the number is:-",sum2)  