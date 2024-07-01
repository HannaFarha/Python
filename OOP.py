class Employee:
    number_of_employees =0
    def __init__(self, name, age, salary):
        self.name=name
        self.salary=salary
        self.age = age
        Employee.number_of_employees +=1

    def greeting(self):
        print("Hi, my name is {} ".format(self.name))


class secundEmployee(Employee):
    def local_greeting(self):
        print("Ola")
        self.greeting()
class thirdEmployee(Employee):
    def local_greeting(self):
        print("Ola Ola")
        self.greeting()
class Hotel:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.employees =[]
    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees

e1 = Employee("Johnny",25,10000)
print("Nummber of Employees = {}".format(Employee.number_of_employees))
e2=Employee("Hanna",42,1000)
print("Nummber of Employees = {}".format(Employee.number_of_employees))
e3 = Employee("Johny",24,100)
print("Nummber of Employees = {}".format(Employee.number_of_employees))
e4=Employee("Hana",43,10090)
print("Nummber of Employees = {}".format(Employee.number_of_employees))
e5 = secundEmployee("Johnny",25,10000)
print("Nummber of Employees = {}".format(Employee.number_of_employees))
e6= secundEmployee("Hanna",42,1000)
print("Nummber of Employees = {}".format(Employee.number_of_employees))
e7 = thirdEmployee("Johny",24,100)
print("Nummber of Employees = {}".format(Employee.number_of_employees))
e8=thirdEmployee("Hana",43,10090)

h1=Hotel("ysdkk","Germany")
h2=Hotel("ysdkko","Syria")
h1.add_employee(e1)
h1.add_employee(e2)
h2.add_employee(e3)
h2.add_employee(e4)
print("Germany sum = {}".format(sum([x.salary for x in h1.get_employees()])))
print("Syria sum = {}".format(sum([x.salary for x in h2.get_employees()])))

print([x.salary for x in h1.get_employees()])
print([x.salary for x in h2.get_employees()])

e5.local_greeting()
e7.local_greeting()