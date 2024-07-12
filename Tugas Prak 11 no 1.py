class Employee:
    'Common base class For all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Employee %d" %Employee.empCount)
    def displayEmployee(self):
        print("Name :", self.name, ", Salary :", self.salary)

#This would create first object Employee class"
emp1 = Employee("Zara", 2000)
#This would create second object Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)
print("")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello nama saya :", self.name)
        print("Umur saya :", self.age)

p1 = Person("Budi", 19)
p1.myfunc()
