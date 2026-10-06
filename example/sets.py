# my_set = {1, 2, 2, 1, "adasas", "adasas"}

# my_set = set("hello")

# my_set = set([1, 2, 3, 3, 4, 4, 4, 5, 4, 3, 2, 1])

# my_set = set()

# my_set.add(1)
# my_set.add(2)
# my_set.add(1)

# my_set = {elem for elem in range(10)}

# my_set.update("hello")

# res = my_set.discard(1)

# res = my_set.remove(9)

# # print(f"presult: {res}")

# # my_set.clear()

# print(my_set)
# print(type(my_set))

# print(6 in my_set)

# for elem in my_set:
#     print(elem)

my_set_1 = {elem for elem in range(10)}
my_set_2 = {elem for elem in range(10, 15)}

print(my_set_1)
print(my_set_2)

# result = my_set_1.intersection(my_set_2)
# result = my_set_1 & my_set_2

# my_set_1.update(my_set_2)
# result = my_set_1

# result = my_set_1.union(my_set_2)
# result = my_set_1 | my_set_2

# result = my_set_1.difference(my_set_2)
# result = my_set_2.difference(my_set_1)

# result = my_set_2 - my_set_1

# result = my_set_1.symmetric_difference(my_set_2)
# result = my_set_1 ^ my_set_2

# result = my_set_1.issubset(my_set_2)

# result = my_set_2.issuperset(my_set_1)

result = my_set_1.isdisjoint(my_set_2)

print(result)