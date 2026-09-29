# my_str = "Hello, Python!"

# sep = ", "
# my_list = my_str.split(sep)

# new_str = sep.join(my_list)

# print(new_str)

# list_1 = []
# list_1 = list("Hello!")

# print(list_1)
# print(len(list_1))

# print(list_1[::-1])

# list_1[0: 2] = "hE"

# list_2 = list(range(10))

# print(list_2)

# for elem in list_1:
#     print(elem)


# list_3 = []

# list_3.append("MSK")
# list_3.append("NSK")SK", "SPB"
# list_3.append("SBP")

# list_3.extend(["NSK", "SPB"])

# list_3 += ["NSK", "SPB", 0, True, 0]

# removed_elem = list_3.pop(1)

# print(f"removed_elem: {removed_elem}")

# list_3.insert(1, "Samara")

# print(list_3)

# list_3.remove(0)
# list_3.remove(0)
# list_3.remove(True)

# list_3.clear()

# del list_3

# list_3.reverse()

# result = list_3.sort(reverse=True)

# result = sorted(list_3, reverse=True)

# print(f"result: {result}")

# print(list_3)

# result = list_3.count(0)

# ind = list_3.index("SPB")

# print(list_3)
# print(f"Index: {ind}")
# print("result: ", result)

# for elem in list_3:
#     print(elem)


# new_list_1 = [1, 2, 5, 7]
# new_list_2 = new_list_1.copy()

# new_list_1[-1] = 0

# print(new_list_1)
# print(new_list_2)


num_list = list(range(10))
num_list.append("")

# print(num_list)

# Задача: получить список квадратов чисел из num_list

# new_num_lst = []

# for elem in num_list:
#     if type(elem) == int:
#         res = elem ** 2
#         new_num_lst.append(res)

new_num_lst = [elem ** 2 for elem in num_list if type(elem) == int]

# print(new_num_lst)

# num_list = [1, -5, 100, 23, 18]

# max_value = max(num_list)
# min_value = min(num_list)
# sum_value = sum(num_list)
# avg = sum_value / len(num_list)

# print(f"Max value: {max_value}\nMin value: {min_value}\nSum: {sum_value}\nAVG: {avg}")

# my_str = "hello"

# my_list = [symb.upper() for symb in my_str]

# print("".join(my_list))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [7, 8, 9]

# ll = [l1, l2, l3]

# print(ll)
# # print(ll[1][0])

# for elem in ll:
#     for sub_elem in elem:
#         print(sub_elem, end=" ")
#     print("\n")

# my_tuple = (1, 2, 4)

my_tuple = tuple([1, 2, 3])


print(my_tuple)
print(type(my_tuple))
# my_tuple[-1] = 8

print(my_tuple[-1])