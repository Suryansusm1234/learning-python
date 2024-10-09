#Making A kbc game in python
import math
q = ["What is the capital of India?",'Who is known as the "Father of the Nation" in India?',"Which is the national bird of India?","Who is the current CM of Odisha?","Which river is considered the holiest in India?"]
opt=["Delhi","Kolkata","Mumbai","Bihar","SRK","Salman Bhai","Mahatma Gandhi","Virat Kohli","Modi Ji","Peacock","Crow","Sparrow","Navien Patnayak","Biju Patnaik","Binayak Acharya","Mohan Charan Majhi","Yamuna","Godavari","Krishna","Ganga"]
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
        for i in range(0,5):
            print(f"Question {i+1}: {q[i]}:-")
            print(f"{1}.{opt[a]}\t\t",f" {2}.{opt[a+1]}\t\t",f"{3}.{opt[a+2]}\t\t",f"{4}.{opt[a+3]}")
            ans= int(input("Enter Your answer:-"))
            if((i == 0 and ans ==1)or(i == 1 and ans ==3)or (i ==2 and ans == 2)or (i == 3 and ans == 4 )or(i ==4 and ans ==4)):
                print("!!!!!!Correct answer!!!!!!!")
                bal = bal+math.pow(10,i)
            else:
                print("-_-Wrong answer-_-")
                bal= bal - 100
                break
            a = a+4
        print("Thank You For Playing The Game!!!!!!!!!")
        print(name,"of",age,"You are Taking Home Rs:-",bal)
    case 2:
        print("Thank You")
    case _ :
        print("Invalid Option Entered")
