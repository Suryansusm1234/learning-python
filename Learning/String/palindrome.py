userstring = input("Enter a string to check if it spalindrome or not:-").lower()
userreverse = ''.join(reversed(userstring))
if (userstring== userreverse):
    print("The string is a palindrome")
else:
    print("It is not a palindrome")