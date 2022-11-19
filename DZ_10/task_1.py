def season():
    global time
    try:
        x = int(input('Введіть номер місяця: '))
        if x <= 0 or x > 12:
            raise ValueError()
        elif x == 12 and 1 <= x >= 2:
            time = 'Зима'
        elif x >= 3 and x <= 5:
            time = 'Весна'
        elif x >= 6 and x <= 8:
            time = 'Літо'
        elif x >= 9 and x <= 11:
            time = 'Осінь'
        return time
    except ValueError:
        print("Введений не коректний номер місяця!")
    else:
        print("Сталася помилка!")



print(season())
