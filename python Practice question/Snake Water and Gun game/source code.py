import random
computer = ["s", "W","G"]
Name = input("Enter your Name:-")
count =0
tie = 0
lost = 0
for i in range(5):
    user = input("What's your choice? 's' for snake, 'w' for water, 'g' for gun or (q) to quit:  ").lower()
    if user == 'q':
        print("Thanks for playing")
        break
    def play():
        global user
        if user not in ["s", "w", "g"]:
            raise ValueError("Invalid input. Please enter 's', 'w', or 'g'.")
        computer_choice = random.choice(computer).lower()
    
        if user == computer_choice:
            print(f"The computer choiced:-{computer_choice}")
            global tie
            tie+=1
            return 'It\'s a tie'
    
    # r > s, s > w, w > g
        if is_win(user, computer_choice):
            print(f"The computer choiced:-{computer_choice}")
            global count
            count+=1
            return 'You won!'
    
        return print(f"The computer choiced:-{computer_choice}",'You lost!')
    def is_win(player, opponent):
    # return true if player wins
        if (player == 's' and opponent == 'w') or (player == 'w' and opponent == 'g') or (player == 'g' and opponent == 's'):
            return True
        else:
            global lost
            lost+=1

    print(play())
print(f"{Name} won {count} and there is {tie} tie and there is {lost} lost out of 5")

