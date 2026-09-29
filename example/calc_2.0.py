from func import add, div

def request_data():
    action = input("Введите действие: ")
    var_01 = int(input("Первое число :"))
    var_02 = int(input("Второе число :"))

    return action, var_01, var_02


def calc():
    while True:
        action, var_01, var_02 = request_data()

        if action == "+": 
            result = add(var_01 ,var_02) 

        elif action== "/":
            result = div(var_01 ,var_02)

        elif "exit":
            print('Выход')
            break

        print(f"{var_01} {action} {var_02} = {result}")

calc()