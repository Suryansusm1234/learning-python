str = input("Enter a sentence:-")
word = 0
for i in range(0,len(str)):
    word = str.count(" ")
print("The number of words in this sentence is:-",word+1)