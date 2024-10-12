string = input("Enter a string:-")
word_list = string.split(" ")
word_dic = {}
for i in word_list:
    if i not in word_dic:
        word_dic[i]= string.count(i)
for j in word_dic:
    print(f"{j}:{word_dic[j]}")       