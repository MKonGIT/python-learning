# learning python
# def functions
# 19-4-2016 mk

def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''

    # The free line in between is mandatory
    
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)

# at prompt
# help(print)
# 
