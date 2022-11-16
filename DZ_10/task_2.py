num_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def unique_num(lst):
    lst_set = set(lst)
    nonunique_num = []
    try:
        for num in lst_set:
            if not isinstance(num, int):
                raise TypeError
            if lst.count(num) > 1:
                nonunique_num.append(num)
        if len(nonunique_num) >= 1:
            raise ValueError
        return print('Всі числа списку унікальні!')
    except ValueError:
        print(f'Список містить не унікальні числа: {nonunique_num}!')
    except TypeError:
        print('Не всі символи є числами!')


unique_num(num_lst)
