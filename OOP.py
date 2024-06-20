class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.salary=salary
        self.age = age
    def greeting(self):
        print("Hi, my name is {} ".format(self.name))

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
e2=Employee("Hanna",42,1000)
e3 = Employee("Johny",24,100)
e4=Employee("Hana",43,10090)

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