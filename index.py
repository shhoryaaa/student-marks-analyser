def Userput(Id, Name, Subject1, Subject2, Subject3, M1, M2, M3):
    print("Received Name,",Name,"Id=",Id, Subject1,"=",M1, Subject2, "=", M2, Subject3, "=", M3)
    
i=True
for i=True:
    print("1= Enter student mark Details \n 2= See Student Mark Details \n 3= Analyse Marks \n 4=End")
    a=int(input(" :" ))
    if a=1:
        b=input("Enter Student Name: ")
        c=input("Enter Student ID: ")
        s1=input("Subj1: ")
        s2=input("Subj2: ")
        s3=input("Subj3: ")
        Ma1=int(input("Marks of", s1))
        Ma2=int(input("Marks of", s2))
        Ma3=int(input("Marks of", s3))
        Userput(c,b,s1,s2,s3,Ma1,Ma2,Ma3)
        continue
        i=False
        