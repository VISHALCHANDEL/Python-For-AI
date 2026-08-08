print("=================Student Record Manager ======================")
print("1. Add Student")
print("2. Search Student")
print("3. Update Marks")
print("4. Delete Student")
print("5. Show All Students")
print("6. Exit")

i = int(input("Enter Choice: "))

list = []
while(i != 6):

    if(i == 1):
        id   = int(input("Enter id of Student: "))
        name = input("Enter student name: ")
        marks = input("Enter marks of student: ")
        list.append([id, name, marks])

    elif i == 2:
        id = int(input("Enter student id: "))
        notFound = True
        for l in list:
            if l[0] == id:
                print('Student is found in Record')
                notFound = False
        if notFound:
            print("Student is not found in the Student Record")


    elif i == 3:
        id = int(input("Enter student id: "))
        for l in list:
            if(l[0] == id):
                marks = int(input("Enter new marks:"))
                l[2] = marks
                print("Marks Updated succesfully")


    elif i == 4:
        id = int(input("Enter Student id: "))
        i = 0
        listLen = len(list)
        while(i < listLen):
            if list[i][0] == id:
                list.pop(i)
                print("Student Deleted sucessfully")
            i += 1

    elif i == 5:
        print("======================= Students Details ===========================")
        for l in list:
            print(f'Id: {l[0]} Name: {l[1]} Marks: {l[2]}')


    print("=============== Welcome Again ===============")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Show All Students")
    print("6. Exit")

    i = int(input("Enter Choice: "))