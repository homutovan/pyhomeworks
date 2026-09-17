num = int(input("Enter a number:"))

for number in range(1, num + 1):

    if number == 1:
        print(number, "Number is not simple")
        continue

    elif number == 2:
        print(number, "Number is simple")
        continue

    else:
        not_simple = False

        for elem in range(2, number):
            if not number % elem:
                print(number, "Number is not simple")
                not_simple=True
                break

        if not not_simple:
            print(number, "Number is simple")
        
