# 181 True
# 335 False

number = int(input("Enter a number:"))

sign_1 = number // 100
sign_3 = number % 10

print(sign_1, sign_3)

if sign_1 == sign_3:
    print("Number is palindrom")
else:
    print("Number is not palindrom")

