#Making A kbc game in python
import math
with open("question.txt","r") as f:
    q = list(f.readlines())
with open('answer.txt', 'r') as f:
      opt = [line.strip() for line in f.readlines()]
prize=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
str="Welcome to KBC By suryansu"
print(str.center(50,"!"))
print("Press 1 if You want to play the game")
print("Press 2 if you want to exit")
i = int(input("Enter Your choice:-"))
a = 0
bal = 0
match i:
    case 1:
        name= input("Enter Your Name:-")
        age = int(input("Enter Your age:-"))
        for j in range(0,10):
            print(f"Question {j+1}: {q[j]}")
            print(f"{1}.{opt[a]}\t"f"{2}.{opt[a+1]}\t"f"{3}.{opt[a+2]}\t"f"{4}.{opt[a+3]}")
            
            ans= int(input("Enter Your answer:-"))
            if((j == 0 and ans ==3)or(j == 1 and ans ==1)or (j ==2 and ans == 1)or (j == 3 and ans == 1 )or(j ==4 and ans ==1)or (j==5 and ans == 1)or (j==6 and ans == 1)or (j==7 and ans == 2)or (j==8 and ans == 1)or (j==9 and ans == 3)):
                bal = bal+prize[j]
                print(f"!!!!!!Correct answer!!!!!!! and you won Rs.{prize[j]}")
                
            else:
                print("-_-Wrong answer-_-")
                print("Better Luck Next time")
                print(f"The amount won by you is:-Rs.{bal}")
                break
            a = a+4
        print("!!!!!!!!!!!!Thank You For Playing The Game!!!!!!!!!")
        print(name,"of age ",age,"You are Taking Home Rs:-",bal)
    case 2:
        print("Thank You")
    case _ :
        raise ValueError("You have entered a invalid Option")

