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
  
# class Employee:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
# 
#     def displayEmployee(self):
#         print(self.first_name + " " + self.last_name + " - " + str(self.age) + " years old")
# 
# class Organization:
#     def __init__(self, name, laptops, employees):
#         self.name = name
#         self.laptops = laptops
#         self.employees = employees
#     
#     def displayLaptops(self):
#         for laptop in self.laptops:
#             print(laptop.model)
# 
# class Laptop:
#     def __init__(self, brand, ram, storage, age, model):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#         self.age = age
#         self.model = model
#         
#     def updateLaptop(self, ramUpdated=0, storageUpdated=0, yearUpdated=0):
#         if ramUpdated != 0:
#             self.ram = ramUpdated
#         if storageUpdated != 0:
#             self.storage = storageUpdated
#         if yearUpdated != 0:
#             self.age = yearUpdated
#         
#         if 2025 - self.age >= 5:
#             print("Этот ноутбук слишком старый, его нужно выбросить!")
#     
#     def giveGift(self, organization):
#         print("Передача " + self.model + " организации " + organization.name)
#         organization.laptops.append(self)
# 
# legion = Laptop("Lenovo", 16, 512, 2012, "XP13")
# print(legion.storage)
# legion.updateLaptop(ramUpdated=32)
# print(legion.storage)
# 
# employee1 = Employee("Иван", "Петров", 30)
# employee2 = Employee("Анна", "Сидорова", 25)
# 
# africa2 = Organization("Africa", [], [employee1, employee2])
# 
# 
# for employee in africa2.employees:
#     employee.displayEmployee()
# 
# legion.giveGift(africa2)

#4444444444444444444444444444444444444444444
class CarPark:
    def __init__(self,name):
        pass  # No implementation provided for CarPark, leave it as is

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_broken = False
    
    def breakDown(self):
        self.is_broken = True
    
    def displayInfo(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("year: ", self.year)
        print("seisunnd", self.is_broken)  # Kept the original "seisunnd" text
    
class ServiceCenter:
    def __init__(self, name):
        self.name = name
    
    def carRepair(self, car):
        car.is_broken = False

class Owner:
    def __init__(self, name):
        self.name = name 
        self.cars = []
        
    def aadCars(self, car):  # Keeping your original "aadCars"
        
        self.cars.append(car)
        
    def sendCarsToServaceCenter(self, serviceCenter):  # Kept your "sendCarsToServaceCenter"
        print("Kasutja saatis remondikeskusse sellised autod: ")
        for car in self.cars:
            if car.is_broken:
                car.displayInfo()
                serviceCenter.carRepair(car)

# Example usage
bmwCenter = ServiceCenter("BMW center")
car1 = Car("BMW", "E34", 1990)
car1.breakDown()  # Mark the car as broken
car2 = Car("Feerari", "F40", 1992)
car2.breakDown()  # Mark the car as broken
car3 = Car("Mersedes", "w220", 2005)
car4 = Car("Mersedes", "CLS64", 2024)
car4.breakDown()

MarkZuckerberg = Owner("Mark Zuckerberg")
MarkZuckerberg.aadCars(car1)  # Using "aadCars"
MarkZuckerberg.aadCars(car2)
MarkZuckerberg.aadCars(car3)
MarkZuckerberg.aadCars(car4)
MarkZuckerberg.sendCarsToServaceCenter(bmwCenter)  # Using "sendCarsToServaceCenter"

# After repair


bmwCenter.carRepair(car1)


