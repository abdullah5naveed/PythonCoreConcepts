def find_max(number):
    max_num = number[0]
    for i in number:
        if i > max_num:
            max_num = i
    return max_num


# data = []
# elements = int(input("Enter the number of Element: "))
# for i in range(0, elements):
#     element = int(input(f"Enter you {i} element: "))
#     data.append(element)
# print(data)
# print(find_max(data))