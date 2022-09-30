'''Modul for checking the Fibonacci number'''


def get_fibonacci_num(num):
    '''Function that returns the Fibonacci num'''
    return num if num in (0,1) else get_fibonacci_num(num-1) + get_fibonacci_num(num-2)

print(get_fibonacci_num(10))


def get_fibonacci_first_ten_numbers():
    '''Function that returns the fibonacci numbers from 0 to 10 and append them to list'''
    num = 10
    fibonacci = [0, 1]
    fibonacci += [(fibonacci := [fibonacci[1], fibonacci[0]
                    + fibonacci[1]]) and fibonacci[1] for k in range(num-2)]
    return fibonacci

print (get_fibonacci_first_ten_numbers())
