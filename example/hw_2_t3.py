# N < 100

number = 100

while True:
    request_number = int(number / 2)
    user_answer = input(f"Ваше число больше {request_number}? (да/нет):")

    if user_answer == "да":
        number = number + request_number
    elif user_answer == "нет":
        number = request_number
    elif user_answer == "это оно":
        print(f"Я угадал ваше число! Это {request_number}!")
