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

