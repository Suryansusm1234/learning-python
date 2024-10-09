a = input("Enter A number between 5 and 9:-")
b = "quit"
if(a == b or a ==b.upper()):
    pass
else:
    a = int(a)
    if(a>=5 and a <=9):
        print("Good you did a great job")
    else:
        raise ValueError("The number should be between 5 and 9")

