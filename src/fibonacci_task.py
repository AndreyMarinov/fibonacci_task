'''Modul for checking the Fibonacci number'''


def get_fibonacci_num(num) -> int:
    '''Function that returns the Fibonacci num
    
    :param: num:  value that is used to calculate the fibonacci number
    :return: int: when calculating the fibonacci number
    '''
    return num if num in (0,1) else get_fibonacci_num(num-1) + get_fibonacci_num(num-2)


def get_fibonacci_first_ten_numbers() -> list:
    '''Function that returns the fibonacci numbers from 0 to 10 and append them to list
    
    :return: list with the first 10 fibonacci numbers
    '''
    num = 10
    fibonacci = [0, 1]
    fibonacci += [(fibonacci := [fibonacci[1], fibonacci[0]
                    + fibonacci[1]]) and fibonacci[1] for k in range(num-2)]
    return fibonacci
