num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter second num:"))
num_3 = int(input("Enter 3 num:"))

max_num = 0

if num_1 > num_2 and num_1 > num_3:
    max_num = num_1
elif num_2 > num_1 and num_2 > num_3:
    max_num = num_2
else:
    max_num = num_3
print("Max num is:", max_num)