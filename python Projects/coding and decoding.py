#To create a program which can code or decode a massage entered by the user
#Rules of the code language:
#if the word have 3 letter then it remove the first letter and add it to the end of the word and add 3 random letter at the begining and the end of the word
#if the word have 2 letter then it just simplely reverse the given word
#Rules for decoding the sereate code:
#it just undo all the process that were carried out to code the message 
#Note:-It just give the required decoded message if it was coded using the following coder of the program else no required output is found
import random
import string
def coding():
    str = input("Enter Your Message:-")
    text =str.split(" ")#to separate the words of the given string 
    for i in range(len(text)):
        if(len(text[i])>=3):
            str1 = text[i][0]#to separate the first letter to add it to the end 
            str2 = text[i][1:]+str1
            str2 = ''.join(random.choice(string.ascii_letters) for _ in range(3))+str2+''.join(random.choice(string.ascii_letters) for _ in range(3)) 
            text[i]=str2
        else :
            if(len(text[i]) ==2):
                separate =text[i][0]
                newstring = text[i][1:]+separate
                text[i]=newstring
    for j in range(len(text)):
        print(text[j],end=(" "))
def decoding():
    str = input("Enter the message to decode:-")
    text2 = str.split(" ")
    for i in range(len(text2)):
        if(len(text2[i])>=3):
            st1 = text2[i][3:-3]
            text2[i]=st1[len(st1)-1]+ st1[:len(st1)-1]
        else:
           if(len(text2[i])==2):
               st2=text2[i]
               text2[i] = st2[::-1]
    for j in range(len(text2)):
        print(text2[j],end=(" "))
print("Enter 1 to code a Message")
print("Enter 2 to decode a message")
a = int(input("Enter Your Choice:- "))
match a:
    case 1 :
        coding()
    case 2 :
        decoding()
    case _ :
        raise TypeError("Invalid Option Enter!!!!!")
