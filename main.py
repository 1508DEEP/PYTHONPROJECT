# print("Hello World")

# x = 5
# y = "John"
# print(x)
# print(y)

# x = 5
# x = "John"
# x = "Deep"
# print(x)

# x = str(3)
# y = int(3)
# z = float(3)
# print(x)
# print(y)
# print(z)

# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# x,y,z = "Deep","Grishkumar","Patel"
# print(x)
# print(y)
# print(z)

# x = y = z = "Deep"
# print(x)
# print(y)
# print(z)

# Name = ["Deep", "Grishkumar", "Patel"]
# x, y, z = Name
# print(x)
# print(y)
# print(z)
# print(type(Name))

# x = "My name"
# y = "is"
# z = "Deep Girishkumar Patel"
# print(x, y, z)
# print(x + y + z)

# OUTPUT ?
# You can not combine different data type
# x = 5
# y = "Deep Girishkumar Patel"
# print(x + y)

# OUTPUT ?
# x = "DEEP GIRISHKUMAR"
# def myfunc():
#     print(x + "Patel")
#     myfunc()

# a = "Hello World"
# b = 20
# c = 20.5
# d = 1j
# e = ["apple", "banana", "cherry"]
# f = ("apple", "banana", "cherry")
# g = range(6)
# h = {"name" : "John", "age" : 36}
# i = {"apple", "banana", "cherry"}
# j = frozenset({"apple", "banana", "cherry"})
# k = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))
# print(type(i))
# print(type(j))
# print(type(k))

# a = "Hello world!"
# print(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11])

# for a in "Deep" :
#     print(a)

# a = "Hello World!"
# print(len(a))

# Check if it is true or not .
# txt = "The best things in life are not free!"
# print("expensive" not in txt)

# OUTPUT ?
# a = "Hello World!"
# print(a[2:5])

# x = "Hello World!"
# print(x.upper())

# Removes space in the begining of variable
# a = "     Hello, world!    "
# print(a.strip())

# a = "Yello, World!"
# print(a.replace("Y","H"))

# a = "Hello, World!"
# print(a.split(","))

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# age = 27
# txt = "My name is Deep, and I am {}"
# print(txt.format(age))

# CODE FOR CALCULATOR

# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# def multiply(x, y):
#     return x * y
#
# def divide(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Error: Division by zero"
#
# def percentage(x, y):
#     return (x * y)/ 100
#
# def calculator():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Percentage")
#
#     choice = input("Enter choice (1/2/3/4/5): ")
#
#     if choice in ('1', '2', '3', '4', '5'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#
#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
#         elif choice == '5':
#             print(num1, "% of", num2, "=", percentage(num1, num2))
#     else:
#         print("Invalid input")
#
# calculator()



# from datetime import datetime
#
# # Ask the user to input their birthdate
# birthdate_str = input("Please enter your birthdate (YYYY-MM-DD): ")
#
# # Convert the input string to a datetime object
# try:
#     birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
# except ValueError:
#     print("Invalid date format. Please use YYYY-MM-DD.")
#     exit()
#
# # Get today's date
# today = datetime.now().date()
#
# # Calculate the difference in days
# difference = today - birthdate
#
# # Access the days from the difference
# total_days = difference.days
#
# print(f'Total number of days since your birth: {total_days} days')


# Prime number
num = int(input("Enter a number: "))

if num >= 2:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")