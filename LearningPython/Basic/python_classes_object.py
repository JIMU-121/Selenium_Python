
class Employee:

    def __int__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def greet_person(self):
        print("Hello, welcome to RCV Academy "+self.fname)


emp1 = Employee('Souvik', 'Bhatt', 'mv@rcvacademy.com')
# emp2 = Employee()

print(emp1.fname)
