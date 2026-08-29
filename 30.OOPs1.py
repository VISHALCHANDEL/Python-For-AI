class faculty:
    def putdata(self):
        self.id = int(input("Enter faculty id: "))
        self.name = input("Enter name:")
        self.salary = float(input("Enter faculty salary: "))

    def display(self):
        print("Faculty id: ", self.id)
        print("Faculty name: ", self.name)
        print("Faculty salary: ",self.salary)


a = faculty()
a.putdata()
a.display()
