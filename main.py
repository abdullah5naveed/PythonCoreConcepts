# name = "john Smith"
# age = 20
# is_new = True
# print(name, age, is_new)

# name = input("What is your name? ")
# color = input("Whats your favrt color? ")
# print(name + " likes " + color)

# weight = input("Enter your Weight in Kilo-grams: ")
# print(type(weight))
# weight_pounds = float(weight) * 2.205
# print(type(weight_pounds))
# print("Your weight in pounds is: ", weight_pounds)

    ##logical Operators
# price = 1000000
# is_good_credit = True
# if is_good_credit:
#     n_price = 0.1 * price
# else:
#     n_price = 0.2 * price
# print(f"Down payment is: ${n_price}")

    ##Comparison Operatores
# name = input("Enter Your Name: ")
# if len(name) < 3:
#     print("Name is too short.")
# elif len(name) > 50:
#     print("Name is too long")
# else:
#     print("name looks good...")

    ## Weight Converter
# weight = int(input("Enter you weight: "))
# unit = input("Is that weight in lbs(L) or kilograms(K): ")
#
# if unit.upper() == "L":
#     c_weight = weight * 0.45
#     print(f"your weight in kilograms: {c_weight}")
# elif unit.upper() == "K":
#     c_weight = weight / 0.45
#     print(f"your weight in pounds: {c_weight}")
# else:
#     print("Kindly enter a correct value.")

    ##While Loop
# i = 1
# while i <= 5:
#     print('#' * i)
#     i += 1
# print("Done...")

    ## Gessing Game --- While / else
# secret_number = 7
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     try:
#         guess = int(input("Guess the Number: "))
#     except ValueError:
#         print("only enter a numaric value")
#     guess_count += 1
#     if guess == secret_number:
#         print("You win...")
#         break
# else:
#     print("You Loss...")

    ## Car Game
# command = ""
# started = False
# while True:
#     command = input("Enter Command: ").upper()
#     if command == "HELP":
#         print("""
#         Start - to start car
#         Stop - to stop car
#         exit - to exit
#         """)
#     elif command == "START":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("car is started... Ready to Go")
#     elif command == "STOP":
#         if not started:
#             print("Car is already stoped")
#         else:
#             started = False
#             print("car is stoped")
#     elif command == "EXIT":
#         break
#     else:
#         print("I don't understand the command")

    ##For Loop

# for item in "python":
#     print(item)

# ###Range function is taking 3 values, 1st starting number, 2nd ending number, 3rd jumping value
# for item in range(1, 10, 2):
#     print(item)

# cart = [10, 30, 40, 80]
# total = 0
# for item in cart:
#     total += item
# print(total)

    ##Nested Loop
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

#print F in nested Loop
# number = [5,2,5,2,2]
# for item in number:
#     output = ''
#     for y in range(item):
#         output += "X"
#     print(output)

    ## List
# students = ['ali', 'umair', 'umar', 'Sami', 'sohail', 'akbar']
# print(students[1:10])
# #to modify any index of list
# students[0] = 'abdullah'
# print(students)
# print(students[0])

#Find Large Number
# numbers = [45, 356, 53262, 234, 423, 3252553254, 4532, 57, 123]
# large_number = 0
# for i in numbers:
#     if i > large_number:
#         large_number = i
# print(large_number)

    ## 2-D List
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][1] = 25
# # print(matrix[0][1])
# for x in matrix:
#     for y in x:
#         print(y)

#     #List Methods
# numbers = [20, 30, 40, 50]
# print(numbers)
# #add new item to list
# numbers.append(60)
# print(numbers)
# #add new item at specific index
# numbers.insert(0, 100)
# print(numbers)
# #remove any item from list
# numbers.remove(100)
# print(numbers)
# #Remove last value of the list or from any index
# numbers.pop(1)
# print(numbers)
# #to check index of any item in list
# print(numbers.index(50))
# #another way to check
# print(40 in numbers)
# #to cont the occurence of an item
# print(numbers.count(20))
# #to sort the items of list
# numbers.sort()
# numbers.reverse()
# print(numbers)
# #Make copy of list
# nums = numbers.copy()
# print(f"THis is copy: {nums}")
# #remove all items from list
# numbers.clear()
# print(numbers)

# Remove Duplicated from list
# numbers = [2, 4, 6, 8, 6, 10, 20, 10, 4, 34, 2]
# for i in numbers:
#     if numbers.count(i) >= 2:
#         numbers.remove(i)
# print(numbers)
# # another way
# numbers = [2, 4, 6, 8, 6, 10, 20, 10, 4, 34, 2]
# unique =[]
# for i in numbers:
#     if i not in unique:
#         unique.append(i)
# print(unique)

    ##Tuples
#tuples are immutable, or can not b changed
# numbers = (1, 2, 3, 4)
# print(numbers.count(2))
#
# #unpacking
# numbers = [1, 2, 3]
# #or
# numbers = (5, 6, 7)
# x, y, z = numbers
# print(x)
# print(y)
# print(z)

    ##Dictionary
# students = {
#     "name" : "Ali",
#     "age" : 20,
#     "is_register" : True
# }
# # print(students['name'])
# #another Way
# print(students.get('is_rgister', "this Key is not available"))
# #update or add new item in Dictionary
# students['dob'] = '24-oct,1994'
# print(students.get('dob'))

#Detect the enter Number
numbers = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}
phone = input("Enter the numbers: ")
output = ''
for i in phone:
    output += numbers.get(i, '!') + " "

print(output)
