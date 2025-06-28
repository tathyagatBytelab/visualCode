# print("Hello, world!")
# print(5 + 3)
# print("My age next year will be", 20 + 1)

# name = "Amit"
# age = 21
# price = 49.99
# is_student = True

# print("Name:", name)
# print("Age:", age)
# print("Price:", price)
# print("Student:", is_student)

#taking input from the user 
# name = input("waht is you name")
# print("hello",name)

# age = input("Enter your age: ")
# print("Your age next year will be:", int(age) + 1)

# name = input("Enter your name: ")
# city = input("Where do you live? ")
# age = int(input("How old are you? "))

# print("\n--- Summary ---")
# print("Name:", name)
# print("City:", city)
# print("Age:", age)
# print("Next year you will be", age + 1)


# num1 = int(input("enter the number1 "))
# num2 = int(input("enter the number2 "))

# print("sum",num1+num2)
# print("difference",num1-num2)
# print("product",num1*num2)


# fruits = "Apple", "Banana", "Mango", "Guava"
# Vegetables = "Gourd", "ladiesfinger", "Spnich", "potato", "Tomato"
# grocery_item = input("enter the grocery item ")
# for fruit in fruits:
#  if grocery_item == fruit:
#   print(f"{grocery_item} comes under fruits.")
#   found = True
#   break
 
# if not found:
#    for veg in Vegetables:
#      if grocery_item == veg:
#        print(f"{grocery_item} comes under Vegetable.")
#        found = True
#        break
# if not found:
#   print(f"I am sorry the {grocery_item} item is not found in the list under furits and vergetable")  
#   found = False
   

# fruits = ["Mango", "Banana", "Papaya"]
# vegetables = ["Bean", "Cucumber", "Spnich"]
# grocery_item = input("Enter the gocrey item from the list ")
# if grocery_item in fruits: 
#     print(f"{grocery_item} comes under the fruits .")
# elif grocery_item in vegetables:
#     print(f"{grocery_item} comes under vegetables.")   
# else:
#     print("sorry i dont know the {grocery_item} not found in list of fruits and vegetables")    


# age = int(input("Enter your Age "))
# if age > 18:
#     print("you are adult")
# else:
#     print("you are teen")

# marks = int(input("Enter the marks of the student "))
# if marks>=90:
#  print("Grade A")
# elif marks>=75:
#  print("Grade B")
# elif marks>=50:
#  print("Grade is C")
# else:
#  print("fail")

# num1 = float(input("enter the number "))
# if num1 % 2 == 0:
#     print("the number is even") 
# else:
#     print("the number is  odd")
 
# age = int(input("Enter you age "))
# if age>=50:
#     print("you are a old ")
# elif age>=25:
#     print("you are a adult")
# elif age>=15 and age<=25:
#     print("You are teen ")
# else:
#     print("you are child")

# count = 5
# while count > 0:
#     print(f"Count is: {count}")
#     count -= 1 # Important: Increment count to eventually make the condition False
# print("Loop finished!")

# count = 5
# while count <= 10:
#     print(f"Count is: {count}")
#     count += 1 # Important: Increment count to eventually make the condition False

# print("Loop finished!")

# # Example of user input validation
# password = ""
# while password != "secret":
#     password = input("Enter the password: ")
#     if password != "secret":
#         print("Incorrect password. Try again.")
# print("Access granted!")


# wifi_password = ""
# while wifi_password != "techworld@":
#     wifi_password = input("Enter the passowrd : ")
#     if wifi_password != "techworld@":
#        print ("password is incorrect . Try again Sir/Madam")
# print("acced is granted ! good luck ") 


# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(fruit)


# # Iterating over a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# # Iterating over a string
# name = "Python"
# for char in name:
#     print(char)

# # Iterating over a range of numbers (0 to 4)
# for i in range(5): # range(5) generates numbers 0, 1, 2, 3, 4
#     print(i)

# # Iterating with index using enumerate
# my_list = ["a", "b", "c"]
# for index, value in enumerate(my_list):
#     print(f"Index: {index}, Value: {value}")    


# Table = int(input("Enter any number "))
# Multiply = 1
# while Multiply <= 10:
#     result = Table*Multiply
#     print(result ,end="  " )
#     Multiply += 1
 
# Table = int(input("Enter a number "))
# for i in range(1,11):
#     result=Table*i
#     print(result)


# fruits = ["apple", "mango", "banana", "kiwi"]
# fruits.append("carrot")
# fruits.append("avacardo")
# fruits.remove("apple") #remove items from the list 
# fruits.pop(1)
# print(fruits)

# def greet():
#     print("hello this is my function ")
# greet()

# def intro():
#     print("i am learning python , the topic is function ")
#     print("On day i will become a great coder ")
# intro()

# def greet_user(name):
#     print("Hello how are you", name)
# greet_user("Deepak")


# def welcome(name, city):
#     print("hello",name , "your most welcom in", city)
# name = input("Enter your name: ")
# city = input("Enter your city: ")
# welcome(name, city)

# def add(a, b):
#     return a + b
# result = add(5, 3)
# print("Sum is:", result) 

# def operations(a, b):
#     return a + b, a - b, a * b

# s, d, m = operations(10, 5)
# print("Sum:", s)
# print("Diff:", d)
# print("Mul:", m)

# def myfunction(fname):
#     print(fname + " Refnes ")
# myfunction("Email")
# myfunction("Deepak")
# myfunction("Linux")

# def myfunction(fname, lastname):
#     print(fname,+" "+lastname)
# print("Emil")

# def my_function(*kids):
#     print("the youngest chile is ", kids[4])
# my_function("Rohit","Ankit", "Sumit", "vishal ","Deepak")

# def my_function(child1, child2, child3):
#     print("the youngest child is ", child3)
# my_function(child1 ="Rohit", child2 ="Ankit", child3 ="Deepak")

# def my_function(**kid):
#     print("His last name is " +kid["lname"])
# my_function(fname = "Deepak", lname = "Singh")

# def my_function(country = "Norway"):
#     print("I am from " + country)
# my_function("Russia")
# my_function("China")
# my_function()
# my_function("India")

# def myfunction(food):
#     for x in food:
#         print(x)
# fruits = ["mango", "chery", "leechi"]
# myfunction(fruits)

# def myfunction(X):
#     return 5*X
# print(myfunction(3))
# print(myfunction(2))
# print(myfunction(4))
# print(myfunction(9))

# def myfunction():
#     pass
# myfunction()

# def myfunction(x,/):
#     print(x)
# myfunction(3)

# def myfunction(a,b):
#     return
# result = 5 + 6
# print("The sum is : ",result)
    
# def sub(a, b):
#     return a-b
# result = sub(8 , 9)
# print("the sum is : ",result)

# def add(a, b):
#     return a - b
# result = add(5, 3)
# print("Sum is:", result)

# def total(*numbers):
#     sum_ = 0
#     for num in numbers:
#         sum_ += num
#     print("Total:", sum_)
# total(1, 2, 3)
# total(5, 10, 15, 20)

# def total(*number):
#     sum = 0
#     for num in number:
#         sum += num
#     print("total: ", sum)
# total(1, 6, 0)
# total(0, 7, 5, 9)

# def display_info(**data):
#     for key , value in data.items():
#      print(key  , ":" ,  value)
# display_info(name="avmit", age=22, city="Mumbai")


# def greet_user(name, language="English"):
#     if language == "English":
#         print("Hello", name)
#     elif language == "Hindi":
#         print("Namaste", name)
#     elif language == "Spanish":
#         print("Hola", name)
#     else:
#         print("Hi", name)

# # Try calling it:
# greet_user("Amit")                 # Default language (English)
# greet_user("Amit", "Hindi")       # Hindi greeting
# greet_user("Amit", "Spanish")     # Spanish greeting


# def average(*numbers):
#     if len(numbers) == 0:
#         return 0
#     total = sum(numbers)
#     return total / len(numbers)

# # Try calling it:
# print("Average:", average(10, 20, 30))     # Output: 20.0
# print("Average:", average(5, 15, 25, 35))  # Output: 20.0


# def describe_person(**info):
#     for key, value in info.items():
#         print(key + ":", value)

# # Try calling it:
# describe_person(name="Amit", age=21, city="Delhi", hobby="coding")


# name = "AMIT"
# print (len(name))
# print((name).lower())
# print((name).upper())
 
# for ch in "python":
#     print(ch)


