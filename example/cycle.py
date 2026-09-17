# while True:

#     request = input("Продолжаем? (да/нет):")

#     if request == "нет":
#        break

# count = 0

# while True:

#     count += 1

#     if count > 20:
#         break

#     if not count % 2:
#         print("Четное число:", count)
#         continue

#     print("Нечетное число:", count)

summa = 0

for count in range(0, 101, 1):

    print("count:", count)
    summa += count

print("Sum:", summa)


