print("Уместно ли отправлять аудиосообщения?")
condition_1 = int(input("Вам оторвало руки?"))

if condition_1 == 0:
    print("Не уместно")
else:
    condition_2 = int(input("И ноги?"))

    if condition_2 == 0:
        print("Не уместно")

    else:
        print("Ну тогда ладно")