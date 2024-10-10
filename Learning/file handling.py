list = [0]*10
for i in range(10):
    list[i]=int(input(f"Enter the marks of the student {i+1}: "))
with open('myfile.txt','w') as f:
    for i in range(10):
        f.write(f"Student {i+1}: {list[i]}\n")  
f =open('myfile.txt','r')
while True:
    l = f.readline()
    if not l:
        break
    print(l)
f.close()
