print("============ Student Record Manager ============")

while(1):
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Marks")
    print("6. Exit")




    a = int(input("Enter your choice"))


    if a == 1:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = int(input("Enter Marks: "))

        file = open('student.txt', 'a')
        file.write(str(id) + " ")
        file.write(name + " ")
        file.write(str(age) + " ")
        file.write(str(marks) + ' ')
        file.close()

    elif a == 2:
        file = open("student.txt", 'r')

        for line in file:
            print(line)

    elif a == 3:

        id = int(input("Enter id of student:"))

        file = open("Practice/student.txt", 'r')

        for line in file:
            if id in line:
                data = file.readline()
                print(data)
    elif a == 4:
        break

        

        
