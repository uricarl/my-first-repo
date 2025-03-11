from Student import Student
from Employee import Employee

student = Student("Gilad", 25, "Agricalture", 1 ,91)
print("This from programmer 1")
# student.foo()

employee = Employee("John", 40, "Software Engineer", 45000)
people = [student, employee]
for person in people:
    person.printMyself()









