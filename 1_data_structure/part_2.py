

def calculate_meters(distance_in_centimeters):

    meters = distance_in_centimeters // 100
    return meters

def calculate_tonnes(mass_in_kilograms):

    tonnes = mass_in_kilograms // 1000
    return tonnes

def calculate_kilobytes(file_size_in_bytes):

    kilobytes = file_size_in_bytes // 1024
    return kilobytes

def calculate_segments(A, B):

    segments = A // B
    return segments

def calculate_remainder_length(A, B):

    remainder_length = A % B
    return remainder_length

def split_digits(number):

    if 10 <= number <= 99:
        tens = number // 10
        units = number % 10
        return tens, units
    else:
        return 'Введите 2-хзначное число'
    
def calculate_sum_and_product(number):

    if 10 <= number <= 99:
        tens = number // 10
        units = number % 10
        digit_sum = tens + units
        digit_product = tens * units
        return digit_sum, digit_product
    else:
        return 'Введите 2-хзначное число'
    
def swap_digits(number):

    if 10 <= number <= 99:
        tens = number // 10
        units = number % 10
        
        # return int(str(units) + str(tens)) 2-ой вариант
        swapped_number = units * 10 + tens
        return swapped_number
    else:
        return 'Введите 2-хзначное число'
    
def find_hundreds(number):

    if 100 <= number <= 999:
        hundreds = number // 100
        return hundreds
    else:
        return 'Введите 3-хзначное число'

def find_units_and_tens(number):

    if 100 <= number <= 999:
        units = number % 10
        tens = (number // 10) % 10
        return units, tens
    else:
        return 'Введите 3-хзначное число'