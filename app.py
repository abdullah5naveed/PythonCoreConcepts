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


class Dice:
    def role(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return (first, second)


dice1 = Dice()
print(dice1.role())