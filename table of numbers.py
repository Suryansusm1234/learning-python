for i in range(1,11,3):
    for j in range(1,11):
        if(i == 10):
            print(i,"*",j,"=",i*j)
        else:    
         print(i,"*",j,"=",i*j,"\t",i+1,"*",j,"=",(i+1)*j,"\t",i+2,"*",j,"=",(i+2)*i)
    print("\n")