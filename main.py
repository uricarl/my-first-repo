from Student import Student
from Employee import Employee

student = Student("Gilad", 22, "Agricalture", 1 ,91)
# student.foo()

employee = Employee("John", 40, "Software Engineer", 45000)
people = [student, employee]
for person in people:
    person.printMyself()









