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
# class CarPark:
#     def __init__(self,name):
#         pass  # No implementation provided for CarPark, leave it as is
# 
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.is_broken = False
#     
#     def breakDown(self):
#         self.is_broken = True
#     
#     def displayInfo(self):
#         print("Brand: ", self.brand)
#         print("Model: ", self.model)
#         print("year: ", self.year)
#         print("seisunnd", self.is_broken)  # Kept the original "seisunnd" text
#     
# class ServiceCenter:
#     def __init__(self, name):
#         self.name = name
#     
#     def carRepair(self, car):
#         car.is_broken = False
# 
# class Owner:
#     def __init__(self, name):
#         self.name = name 
#         self.cars = []
#         
#     def aadCars(self, car):  # Keeping your original "aadCars"
#         
#         self.cars.append(car)
#         
#     def sendCarsToServaceCenter(self, serviceCenter):  # Kept your "sendCarsToServaceCenter"
#         print("Kasutja saatis remondikeskusse sellised autod: ")
#         for car in self.cars:
#             if car.is_broken:
#                 car.displayInfo()
#                 serviceCenter.carRepair(car)
# 
# # Example usage
# bmwCenter = ServiceCenter("BMW center")
# car1 = Car("BMW", "E34", 1990)
# car1.breakDown()  # Mark the car as broken
# car2 = Car("Feerari", "F40", 1992)
# car2.breakDown()  # Mark the car as broken
# car3 = Car("Mersedes", "w220", 2005)
# car4 = Car("Mersedes", "CLS64", 2024)
# car4.breakDown()
# 
# MarkZuckerberg = Owner("Mark Zuckerberg")
# MarkZuckerberg.aadCars(car1)  # Using "aadCars"
# MarkZuckerberg.aadCars(car2)
# MarkZuckerberg.aadCars(car3)
# MarkZuckerberg.aadCars(car4)
# MarkZuckerberg.sendCarsToServaceCenter(bmwCenter)  # Using "sendCarsToServaceCenter"
# 
# # After repair
# 
# 
# bmwCenter.carRepair(car1)

# #5555555555555555555555555555555555555555555
# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#     def print_person(self):
#         print(self.__name, self.__age)
#         
#     def get_age(self):
#         return self.__age
#     
#     def set_age(self,age):
#         if age<0:
#             print("Viga vanus ei saa olla negatiivne")
#         self.__age = age
# 
# 
# tom = Person("Tom",39)
# tom.__name = "jerry"
# tom.print_person()
# tom.set_age(40)
# tom.print_person()

# 66666666666666666666666666666666666666666666666666666666
# class Student:
#     def __init__(self,name):
#         self.name = name
#         self.__grades = [] #privaatne väli
#         
#     def get_grades(self):
#         return self.__grades
#         
#     def aad_grade(self, grede):
#         self.__grades.append(grede)
#     
#     def avg_grade(self):
#         result = sum(self.__grades)/len(self.__grades)
#         return result
#     
#     def displayInfo(self):
#         print("name: ", self.name,self.__grades)
#         
# class Course:
# #     title
# #     students - privaatne väli
#     def __init__(self, title):
#         self.title = title
#         self.__students = []
#     
#     def add_student(self, student):
#         if isinstance(student, Student):
#             self.__students.append(student)
#         else:
#             print("Ei saa lisada teisi inimesi")
#     def print_students(self):
#         for student in self.__students:
#             print(student.name)
#             
#         
# 
# superStudent = Student("SupeStudent")
# superStudent2 = Student("SupeStudent2")
# superStudent3 = Student("SupeStudent3")
# 
# superStudent.displayInfo()
# superStudent.aad_grade(5)
# superStudent.displayInfo()
# 
# programming = Course("programming")
# programming.add_student(superStudent)
# programming.add_student(superStudent2)
# programming.add_student(superStudent3)
# 
# programming.print_students()
# 
# #777777777777777777777777

# class Animal:
#     def __init__(self,paws,eyes,tail):
#         self.paws = paws
#         self.eyes = eyes
#         self.tail = tail
# 
# class Mammal(Animal):
#     def __init__(self,paws,eyes,tail,name,has_fur):
#         super().__init__(paws,eyes,tail)
#         self.name = name
#         self.has_fur = has_fur
#     
#     def speak(self):
#         print(self.name,"- imetaja")
#         
# class Dogs(Mammal):
#     def __init__(self,paws,eyes,tail,name,has_fur,breed):
#         super().__init__(paws,eyes,tail,name,has_fur)
#         self.breed = breed
#     
#     def speak(self):
#         super().speak()
#         print(self.name,":hav hav")
#         
# pes = Dogs(4,2,1,"Dog",True,"Bobik")
# 
# pes.speak()
# dog = Mammal(4,2,1,"Dog",True)

# # 88888888888888888888888888


# class Vehicle:
#     def __init__(self,bramd,model,milleage):
#         self.bramd = bramd
#         self.model = model
#         self.milleage = milleage
#         
#     def drive(self,miles):
#         self.milleage += miles 
#         
# 
# class Car(Vehicle):
#     def __init__(self,bramd,model,milleage,fuel_type):
#         super().__init__(bramd,model,milleage)
#         self.fuel_type = fuel_type
# 
# class ElectricCar(Car):
#     def __init__(self,bramd,model,milleage,fuel_type,batter):
#         super().__init__(self,bramd,model,milleage,fuel_type)
#         self.batter = batter
#         
#     def drive(self,km):
#         super().drive(km)
#         self.batter -= km
#         
# vehicle = Vehicle("Audi","RS6",2000)
# print(vehicle.milleage)
# vehicle.drive(345)
# print(vehicle.milleage)
# elecElectricCar = ElectricCar("Tesla","cybertruck",100,"electricity",100)
# elecElectricCar.drive(100)
# print(elecElectricCar.milleage)
# print(elecElectricCar.batter)

# # 9999999999999999999999999999999999999999999999999999999999

# class Building:
#     def __init__(self,address,floors,year_built):
#         self.__address = address
#         self.__floors = floors
#         self.__year_built = year_built
#         self.isRenovate = False
#         
#     def displayInfo(self):
#         print(self.__address)
#         print(self.__floors)
#         print(self.__year_built)
#         
#     def renovate(self,year):
#         if(self.__year_built>year):
#             print("ei saa renoveerida hoone")
#         else:
#             self.__year_built = year
#             self.isRenovate = True
# 
# building = Building("Laikmaa 2",5,1100)
# building.displayInfo()
# building.renovate(2000)
# building.displayInfo()
# 
# class Library(Building)
#     def __init__(self,address,floors,year_built,books)
#         super().__init__(address,floors,year_built)
#         self.books = []
#         
#     def displayInfo():
#         super().displayInfo()
#         print("Raamatude arv: ", len(self.books))
#         
#     def list_books(self):
#         for books in self.books:
#             print("Nimetus:", book.title,"author: ",book.author,"year: ",book.year)
#     
#     def borow_book(self,book,data):
#         if boor in self.books:
#             self.books.isBorrowed = True
#             book.date = date
#         else:
#             print("See raamat puudub")
#             
#     def return_book(self,book):
#         self.books.isBorrowed = False
#         
#         
#     def add_book(self,book):
#         self.books.append(book)
#         
# class Book:
#     def __init__(self.title,author,year)
#     self.title = title
#     self.author = author
#     self.year = year
#     self.books.isBorrowed = False
#     self.data = data
#     
#     
# book = Book("Voinna i Mir", "Lev Tolstoi",1867,"23.01.2024")
# liblary = Library("Sõpruse puiestee 182",2,1867)
# liblary.add_book(dook)

# # # 10101010100010101011010000010101010101010011010101010

        
# # class NumderAnalyzer:
# #     def __init__(self,number):
# #         self.__numder = numder
# #         self.NumIsPositive = False
# #         self.numIsEven = False
# # 
# # 
# # class IsEven(self):
# # 
# #     if (__number% 2 == 0 ):
# #         print ( "Четное число" )
# #         self.numIsEven = True
# #     else :
# #         print ( "Нечетное число" )
# # 
# # class IsPositive(self):
# #     if self.__number >= 0:
# #         print("Number is positive")
# #         self.NumIsPositive = True
# #     else:
# #         Print("number is negative")
# #         
# #     
# # 
# # class Summury(self):
# #     print("Your number is: ", self.__number,"positive is : " self.IsPositive, "чотное: ",self.IsEven)


# # 11.11.11.111.11.1.1.11.11.11.11.11.11.11.1.111.111.11.11.11.1.11.1.11.1.


class Person:
    def __init__(self,name,personal_code):
        self.__name = name
        self.__personal_code = personal_code
        self.__add_accounts
        
    def add_accound(self,acounts):
        self.accounts.append(acount)
        
    def get_accounts(self):
        for account in self.__accounts:
            print(account)
        return(self.accounts)
    def get_info(self):
        print(f"personal_code:{self.__personal_code}")
        print(f"name{self.__name}")
       

class BankAccount:
    def __init__(self,account_numder,balance):
        self.__account_numder = account_numder
        self.__balance = balance
    
    def add(self,amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("недостаточно денег")
        else:
            self.__balance -= amount
            print("сняли деньги")
            
    def get_balance(self):
        return self.__balance
    def get_account_number():
        return self.__account_number
    
class Client(Person):
# #     email
# #     phone
# #     clientType(regular,premiu,business)
# #     method account_summary
    
    def __inint__(self,name,personal_code,email,phone,):
        super().__inint__(name,personal_code)
    self.__email = email
    self.__phone = phone
    self.clientType = "Reguular"

    def account_summary(self):
        if self.__balance <= 1000:
            self.clientType = "Regular"
        elif self.__balance > 10000:self.clientType = "premium"
        else:
            self.clientType = "Buisnees"
  
            
            print(f"name:{self.__name}")
            print(f"email:{self.__balance}")
            print(f"phone:{self.__phone}")
            print(f"personal_code{self.__personal_code}")
            print(f"clientType{self.__clientType}")
            
            
            
            
marija = Person("Marija",1234567890,"maria@901gamil.com",+37250394393,"regular")
danil = Person("Danil",1453562234,"danil@901gamil.com",45335477,"regular")
bankAccount = BankAccoutn(123546789,999999999)

marija.account_summary()
 
        
        