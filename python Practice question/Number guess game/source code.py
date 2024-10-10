import random
def welcome():
    print("WELCOME TO THE NUMBER GUESSING GAME")
    print("TRY TO GUESS THE NUMBER I AM THINKING OF FROM 1 TO 100")
def guess():
    global computer_guess
    computer_guess=random.randint(1,100)
    for i in range(10):
        user_guess=int(input("ENTER YOUR GUESS:-"))
        if not (user_guess>=1 and user_guess<=100):
            raise ValueError("Enter a valid number as input")
        if(user_guess - computer_guess >10 or computer_guess - user_guess>10):
            print("TRY AGAIN beacuse the number You have entered is very far from the guessed number")
        elif(user_guess - computer_guess <=10 or computer_guess - user_guess<=10):
            print("The number You have entered is close to the guessed number please try again ")
        elif(user_guess== computer_guess):
            print("YOU HAVE GUESSED THE CORRECT NUMBER")

welcome()
guess()       
print(f"The number guessed By the computer was:-{computer_guess}")