User_input = input("Enter a string:-")
de ={}
for i in User_input:
    de[i] = User_input.count(i)
print(de)