def vowelcheck(j):
    j= j.lower()
    if(j in 'aeiou'):
        return''
    else:
        return j
try:
    User_input =input("Enter A string:-")
    new_String =''.join(map(vowelcheck,User_input))
    print(new_String)
except TypeError:
    print("Please Enter a string")