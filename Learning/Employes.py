information ={}
for i in range(2):
    name = input(f"Enter the name of the {i+1}.employee:-")
    role = input("Enter the role of the employee:-")
    age = input("Enter the age of the employee:-")
    salary= input("Enter the salary of the employee:-")
    information[name] = {"role": role, "age": age, "salary": salary}

for k,(name,details) in enumerate(information.items()):
    print(f"{k+1}.Hello {name} {details['role']} of age {details['age']} you would get a salary of {details['salary']}")
