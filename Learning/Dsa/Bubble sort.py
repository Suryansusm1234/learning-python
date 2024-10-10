import random
list_of_number = [random.randint(1,100) for _ in range(10)]
list_of_number2 = list_of_number
def bubble_sort(list_of_number):
    n = len(list_of_number)
    for i in range(n):
        swap = False
        for j in range(0,n-i-1):
            if list_of_number[j] > list_of_number[j+1]:
                list_of_number[j], list_of_number[j+1] = list_of_number[j+1], list_of_number[j]
                swap = True
        if not swap:
            break
print(list_of_number2)
bubble_sort(list_of_number)
print(list_of_number)