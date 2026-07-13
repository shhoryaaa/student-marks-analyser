def Userput(Id, Name, Subject1, Subject2, Subject3, M1, M2, M3):
    student = {
        "Id": Id,
        "Name": Name,
        "Subject1": Subject1,
        "Subject2": Subject2,
        "Subject3": Subject3,
        "Marks1": M1,
        "Marks2": M2,
        "Marks3": M3
    }

    lst.append(student)
    print("Student details saved successfully.")


def Userout(Id):
    for student in lst:
        if student["Id"] == Id:
            print("\nStudent Found")
            print("ID:", student["Id"])
            print("Name:", student["Name"])
            print(student["Subject1"], "=", student["Marks1"])
            print(student["Subject2"], "=", student["Marks2"])
            print(student["Subject3"], "=", student["Marks3"])
            return

    print("Student not found.")


lst = []

while True:
    print("\n1 = Enter Student Mark Details")
    print("2 = See Student Mark Details")
    print("3 = Analyse Marks")
    print("4 = End")

    a = int(input("Enter your choice: "))

    if a == 1:
        b = input("Enter Student Name: ")
        c = input("Enter Student ID: ")

        s1 = input("Subject 1: ")
        s2 = input("Subject 2: ")
        s3 = input("Subject 3: ")

        print("Marks of", s1)
        Ma1 = int(input())

        print("Marks of", s2)
        Ma2 = int(input())

        print("Marks of", s3)
        Ma3 = int(input())

        Userput(c, b, s1, s2, s3, Ma1, Ma2, Ma3)

    elif a == 2:
        b = input("Enter Student ID: ")
        Userout(b)

    elif a == 3:
        print("Analysis function coming soon.")

    elif a == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")