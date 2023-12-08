
def calculator(input: str):
    try:
        parts = input.split()
        if len(parts) == 3:
            first_num, operation, second_num = parts[:3]
            operation_list = ['+', '-', '*', '/']
            
            if first_num.isdigit() and second_num.isdigit():
                if 1 <= int(first_num) <= 10 and 1 <= int(second_num) <= 10:
                    if operation in operation_list:
                        if operation == '+':
                            return int(first_num) + int(second_num)
                        elif operation == '-':
                            return int(first_num) - int(second_num)
                        elif operation == '*':
                            return int(first_num) * int(second_num)
                        elif operation == '/':
                            return int(first_num) // int(second_num)
                    else:
                        return 'error: Неверная операция'
                else:
                    return 'error: Число вне допустимого диапазона (1-10)'
            else:
                return 'error: Введено не число'  
        else:
            return 'error'  
    except Exception as e:
        raise ValueError(f'Error: {str(e)}')
    
input_name = '6 * 9'
calc = calculator(input_name)   
print(calc)