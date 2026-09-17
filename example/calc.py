# user = input("Ввведите ваше имя:")

var_1 = input("Введите первую переменную:")
var_2 = input("Введите вторую переменную:")

operand = input("Введите операнд")

if operand == "+":
    result = var_1 + var_2

elif operand ==  "-":
    result = var_1 + var_2

# var_2 = int(raw_var_2)

result = int(var_1) + int(var_2)

print(var_1, operand, var_2, "=", result)



