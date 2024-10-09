sum = 0
name = input("Enter the name of the student:-")
age = int(input("Enter the age of the student:-"))
sub = int(input("Enter the number of subjects for which percentage is to be calculated:-"))
for i in range(1,sub +1,1):
    perc = float(input("Enter the marks of the student in subject "+ str(i)+":-"))
    sum +=perc
if(sum/(sub*100)*100 >=50):
    print(name,"of", age ,"is passed")
else:
    print("The student have failed in the examination")    
