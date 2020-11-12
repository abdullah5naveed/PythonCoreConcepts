import random

# for i in range(3):
#     print(random.random())
#
#
# for i in range(3):
#     print(random.randint(10, 30))
#
#
# team = ["ali", "umair", "Usman", "hamza"]
# leader = random.choice(team)
# print(leader)


# class Dice:
#     def role(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return (first, second)
#
#
# dice1 = Dice()
# print(dice1.role())


from pathlib import Path
#absoulte path
#c:\programs\user\....
#/usr/local/bin....

#Relative Path

# path1 = Path("learning")
# print(path1.exists())

# # For creating New directory and Remove
# path1 = Path("address")
# print(path1.mkdir())
# print(path1.rmdir()) #Remove Directory

#to Search all directory
path1 = Path()
for file in path1.glob("*"):
    print(file)


