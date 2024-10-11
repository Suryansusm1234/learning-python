#to find the 2nd largest number from a list
import random
a = [random.randint(1,100) for _ in range(10)]
a.sort()
b = a[-2]
print(a)
print(f"The second largest number in the list is {b}")