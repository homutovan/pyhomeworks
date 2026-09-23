# N < 100

number = 100

# задаем начальный диапазон чисел от 0 до N

th_1 = 0                                            # нижняя граница диапазона поиска     
th_2 = th_1 + number                                # верхняя граница диапазона поиска 
count = 0                                           # счетчик попыток

while th_1 < th_2:
    count += 1
    mean = (th_1 + th_2) // 2                       # середина диапазона поиска 
    print(f"Пробуем угадать число, попытка {count}")
    print(f"Диапазона: {th_1}, {th_2}, середина: {mean}")

    user_answer = input(f"Ваше число больше {mean}? (да/нет):")
    user_answer = user_answer.strip().lower() 

    if user_answer == "да":
        print(f"Загаданное число больше {mean}")
        th_1 = mean + 1                             # число точно больше середины диапазона

    elif user_answer == "нет":
        print(f"Загаданное число меньше {mean}")
        th_2 = mean                                 # число ≤ середины диапазона

    else:
        print("Пожалуйста, ответьте да или нет")
        count -= 1
        continue

    print("\n")

print(f"Ваше число: {th_1}")
print(f"Количество вопросов: {count}")
