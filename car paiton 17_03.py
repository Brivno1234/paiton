# 
# class Car:
#     #konstruktor
#     def __init__(self,color,engine):# atributidww
#         self.color = color
#         self.engine = engine
#         print("autode loomine")
#     def helloSayer(self):
#         print("helo you have " + self.color + " bmv")
# 
# bmv = Car("Black","bensiin")
# bmv2 = Car("Green","electer")
# print(bmv.color)
# print(bmv2.color)
# bmv.helloSayer()
# 
# print()
# print(1111111111111111111111111111111)
# print()
# 
# class person:
#     def __init__(self, hairColor, egeColor, manWomen,):
#         self.hairColor = hairColor
#         self.egeColor = egeColor
#         self.manWomen = manWomen
#     def helloHair(self):
#         print("you have " + self.hairColor + " hair")
#     def helloEge(self):
#         print("you have " + self.hairColor + " ege")
# pipls = person("Black","green","mes")
# pipls2 = person("whigt","brown","mes")
# print(pipls.egeColor)
# print(pipls.manWomen)
# pipls.helloHair
# 
# print()
# print(222222222222222222222222)
# print()
#333333333333333333333333333333333333333333333333333333333
  
class Employee:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def displayEmployee(self):
        print(self.first_name + " " + self.last_name + " - " + str(self.age) + " years old")

class Organization:
    def __init__(self, name, laptops, employees):
        self.name = name
        self.laptops = laptops
        self.employees = employees
    
    def displayLaptops(self):
        for laptop in self.laptops:
            print(laptop.model)

class Laptop:
    def __init__(self, brand, ram, storage, age, model):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.age = age
        self.model = model
        
    def updateLaptop(self, ramUpdated=0, storageUpdated=0, yearUpdated=0):
        if ramUpdated != 0:
            self.ram = ramUpdated
        if storageUpdated != 0:
            self.storage = storageUpdated
        if yearUpdated != 0:
            self.age = yearUpdated
        
        if 2025 - self.age >= 5:
            print("Этот ноутбук слишком старый, его нужно выбросить!")
    
    def giveGift(self, organization):
        print("Передача " + self.model + " организации " + organization.name)
        organization.laptops.append(self)

legion = Laptop("Lenovo", 16, 512, 2012, "XP13")
print(legion.storage)
legion.updateLaptop(ramUpdated=32)
print(legion.storage)

employee1 = Employee("Иван", "Петров", 30)
employee2 = Employee("Анна", "Сидорова", 25)

africa2 = Organization("Africa", [], [employee1, employee2])


for employee in africa2.employees:
    employee.displayEmployee()

legion.giveGift(africa2)
