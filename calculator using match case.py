str = "Welcome to calculator"
str2 = str.title
print(str.center(50,"!"))
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
print("Enter 5 for Modules")
a= int(input("Choice:-"))
match a :
    case 1 :
        b= float(input("Enter 1st number:-"))
        c= float(input("Enter 2nd number:-"))
        print("The sum of the two number is:-",b+c)
    case 2 :
        b= float(input("Enter 1st number:-"))
        c= float(input("Enter 2nd number:-"))
        print("The difference of the two number is:-",b-c)
    case 3 :
        b= float(input("Enter 1st number:-"))
        c= float(input("Enter 2nd number:-"))
        print("The product of the two number is:-",b*c)
    case 4 :
        b= float(input("Enter 1st number:-"))
        c= float(input("Enter 2nd number:-"))
        print("The division of the two number is:-",b/c)
    case 5 :
        b= float(input("Enter 1st number:-"))
        c= float(input("Enter 2nd number:-"))
        print("The modules of the two number is:-",b%c)
    case _ :
        print("Invalid option!!!!!!!!")
print("Thank You")
