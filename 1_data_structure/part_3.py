
def check_positive_num(num: int):
    if num > 0:
        return 'Число является положительным'
    
def check_odd_num(num: int):
    if num % 2 == 1:
        return 'Число является нечетным'
    
def check_even_num(num: int):
    if num % 2 == 0:
        return 'Число является четным'
    
def check_inequality(first_num: int, second_num: int):
    if first_num > 2 and second_num <= 3:
        return 'Справедливы неравенства A > 2 и B ≤ 3'
    
def check_inequality_1(first_num: int, second_num: int):
    if first_num >= 0 and second_num < -2:
        return 'Справедливы неравенства A ≥ 0 или B < -2'
    
def check_inequality_2(first_num: int, second_num: int, third_num: int):
    if first_num < second_num < third_num:
        return 'Справедливо двойное неравенство A < B < C'
    
def check_if_between(first_num: int, second_num: int, third_num: int):
    if first_num < second_num < third_num:
        return 'Число B находится между числами A и C'
    else:
        return 'Число B не находится между числами A и C'
    
def check_odd_nums(first_num: int, second_num: int):
    if first_num % 2 == 1 and second_num % 2 == 1:
        return 'Каждое из чисел A и B нечетное'
    
def check_if_odd_num(first_num: int, second_num: int):
    if first_num % 2 == 1 or second_num % 2 == 1:
        return 'Хотя бы одно из чисел A и B нечетное'
    else:
        return "Оба числа A и B четные"
        
def check_if_one_odd_num(first_num: int, second_num: int):
    if (first_num % 2 != 0 and second_num % 2 == 0) or (first_num % 2 == 0 and second_num % 2 != 0):
        return "Ровно одно из чисел A и B нечетное"
    else:
        return "Условие не выполняется"
    
    
    
