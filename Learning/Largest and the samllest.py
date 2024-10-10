import random 
random_numbers = [random.randint(1, 100) for _ in range(10)]
max= max(random_numbers)#Find the largest number in the list using the python in-build library
min= min(random_numbers)
print(f"The Largest number in the list is:-{max}")
print(f"The smallest number in the list is:-{min}")
print(random_numbers)