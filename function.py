
# a =3
# b =5
# sum = a+b
# print(sum)


# average = (a+b)/2
# print(average)


# def sumFunc():
#     a =4
#     b =8
#     print(a+b)
# sumFunc()
# sumFunc()

# def welcome_message():
#     print("Welcome to python pogrmming")
#     print("Line 2")
# welcome_message()
# welcome_message()
# welcome_message()

# def inspire():
#     print("you are the master of your destiny :Makwana Mayank")
# inspire()

# def good_morning():
#     print("GOOD MORING ,MAKWANA MAYANK")
# good_morning()

# def average(a=10,b=20):
#     averageValue = (a+b)/2
#     print(averageValue)

# average(5,10)
# average(7,10)
# average(80,98)
# average()

# def show_age(name = "makwana",age=22):
#     print(f"My name {name} is and my age {age} ")
# show_age("Mayank",22)
# show_age()
# show_age("ram",25)

# def fun(x):
#     if(x % 4 ==0):
#         print("Even number")
#     else:
#         print("Odd number")
# fun(25)
# fun(24)

# def print_len(list):
#     print(len(list))
# cities =["delhi","nodida","Gujrate","chennai","Mumbai","maharasta"]
# heroes =["thor","ironman","caption","shaktiman"]

# def print_list(list):
#     for item in list:
#      print(item,end=" ") 
# print_list(heroes)



# def cal_fact(n):
#     fact =1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
# cal_fact(6)

# def converter(usd_val):
#     inr_val =usd_val *83
#     print(usd_val,"USD" ,  inr_val, "INR")

# converter(78)
    
# n =int(input("Enter your number :"))
# def cal(n):
    
#         if n % 2 ==0:
#             print("Even number")
#         else:
#             print("Odd number")
# cal(n)



# num = [1,2,3,5,6,8,4]
# num.sort()
# print(num)


# practical 11 in Question = 2

# class Pets:
#     def eat(self):
#         print("Peets eat")

# class Animal(Pets):
#     def sleep(self):
#         print("Animal is sleep")
# class Dog(Animal):
#     def bark(self):
#         print("Dog Bow BOw")

# m =Dog()

# m.eat()
# m.sleep()
# m.bark()

# Practice Set 10 

 # 1
# class Pogrammer:
#     def __init__(self,name,company,salary):
#         self.name =name
#         self.company =company
#         self.salary =salary


#     def Display(self):
#         print("name :", self.name)
#         print("company :",self.company)
#         print("salary :",self.salary)
               

# m1 =Pogrammer("Mayank","Microsoft",5000)
# m2 =Pogrammer("Ram","Microdoft",6000)

# m1.Display()
# m2.Display()

#2

# import math

# class calculator:
#     def __init__(you,num):
#         you.num=num

#     def square(you):
#         print("square =", you.num ** 2)
#     def root(you):
#         print("root =",you.num ** 3)
#     def square_root(you):
#         print("square root =",you.num**0.5)

#     @staticmethod
#     def greet():
#         print("Good day!")

# c =calculator(25)

# c.square()
# c.root()
# c.squar_eroot()
# c.greet()
    
# 3

# class prime:
#     a =7
# obj =prime()

# print("berfore ")
# print("class attribute",prime.a)
# print("object attribute",obj.a)

# obj.a =0

# print("\nafter ")
# print("Class attribute",prime.a)
# print("object attribute", obj.a)


# 4

# class Demo:
#     a =10

#     @staticmethod
#     def greet():
#         print("hello")

# obj = Demo()

# Demo.greet()



# 5 : heirarchicle

# class Animals:
#     pass

# class Pets(Animals):
#     pass


# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Dog is barking!")
        
# obj = Dog()
# obj.bark()


# 6. simple inheritance

    # class TwoD:
    #     def __init__(self, i, j):
    #         self.i = i
    #         self.j = j
    #     def vector2(self):
    #         print(f"{self.i}i + {self.j}j")
            
    # class ThreeD(TwoD):
    #     def __init__(self,i,j,k):
    #         super().__init__(i,j)
    #         self.k=k
            
    #     def vector3(self):
    #         print(f"{self.i}i + {self.j}j +{self.k}k ")
            
    # obj=TwoD(10,5)
    # obj1 =ThreeD(10,5,8)

    # obj.vector2()
    # obj1.vector3()





# 7. Book and EBook

#     Parent class Book
#         title
#         author
#     Child class EBook
#         file_size
#     Display all information.
# class Book:
#     def __init__(self,title,author):
#         self.title =title
#         self.author=author
# class Ebook(Book):
#     def __init__(self, title, author,file_size):
#         super().__init__(title, author)
#         self.file_size =file_size

#     def Display(self):
#         print("Title:",self.title)
#         print("Author:",self.author)
#         print("File_Size:",self.file_size)

# m=Ebook("Pyhton","Guidio van Rossum",15)

# m.Display()

# 8. Laptop and GamingLaptop

#     Parent class:
#         brand
#         RAM
#     Child class:
#         graphics_card
#     Add a method to display complete specifications.

# class Laptop:
#     def __init__(self,brand,Ram):
#         self.b=brand
#         self.r=Ram
# class GamingLaptop(Laptop):
#     def __init__(self, brand, Ram,graphic_card):
#         super().__init__(brand, Ram)
#         self.g=graphic_card

#     def display(self):
#         print("brand:", self.b)
#         print("Ram:" ,self.r)
#         print("graphic_card:",self.g)

# a =GamingLaptop("Asus",8,512)

# a.display()


# Level 4: Challenge

# 9. Teacher and MathTeacher

#     Parent class:
#         name
#         subject
#         method teach()
#     Child class:
#         years_of_experience
#         method solve_math_problem()
#     Display all information.

# class student:
#     def __init__(self,name,subject):
#         self.n =name
#         self.s=subject

#     def teach(self):
#         print("Teacher teaches",self.s)

# class School(student):
#     def __init__(self, name, subject,yers_of_exprience):
#         super().__init__(name, subject)
#         self.y= yers_of_exprience
  
#     def solve_math_problem(self):
#         print("Math teacher solve the problem")

#     def display(self):
#         print("name:" ,self.n)
#         print("subject:",self.s)
#         print("years of expriences:",self.y)

# c=School("Mayank","Python",5)

# c.solve_math_problem()
# c.display()
# c.teach()


# 10. Hospital System

#     Parent class Patient
#         patient_id
#         name
#         age
#     Child class InPatient
#         room_number
#         days_admitted
#         method to calculate bill (days × 2500)


# class Patient:
#     def __init__(self,patient_id,name,age):
#         self.p =patient_id
#         self.n=name
#         self.a=age

# class Inpatient(Patient):
#     def __init__(self,room_number,days_admitted):
#         self.r=room_number
#         self.d=days_admitted

#     def calculate_bill(self):
#         print(self.d*2500)

# h=Inpatient(5, 5)

# h.calculate_bill()


# Bonus Challenge

# 11. Online Shopping
# Create:

#     Parent class Product
#         product_name
#         price
#         display()
#     Child class Electronics
#         warranty (years)
#         discount(percent) that updates the price
#         Display the final price after discount.



# class Product:
#     def __init__(self,product_name,price):
#         self.name=product_name
#         self.price=price
#     def display(self):
#         print(f"Product is {self.name} and product price is {self.price}.")

# class Electronicrs(Product):
#     def __init__(self,warranty,discount,product_name,price):
#         super().__init__(product_name,price)
#         self.w=warranty
#         self.d=discount
#     def display(self):
#         final_price = self.price - (self.price*self.d/100)
#         print("Final price:", final_price )

# e = Electronicrs(2, 5, "Mouse", 500)
# e.display()



# These problems cover the main concepts of simple inheritance:

#     Creating parent and child classes
#     Accessing inherited methods
#     Using constructors (__init__)
#     Using super()
#     Adding new attributes and methods in the child class

# You said:

# class car:
#     def __init__(self ,name,model):
#         self.n =name
#         self.m =model

# class years(car):
#     def __init__(self, name, model,price):
#         super().__init__(name, model)
#         self.p=price
#     @staticmethod
#     def color():
#             print("What is name and model name and color")
    
#     def display(self):
#             print("Name :",self.n)
#             print("model:" ,self.m)
#             print("price:",self.p)

# a =years("Maruti",2020,1500000)
# a.display()
# a.color()



 


