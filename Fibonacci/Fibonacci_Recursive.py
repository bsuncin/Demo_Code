# The goal of this program is to show the exponential
# time complexity of this naive approach to the 
# Fibonacci problem.

#tracks the operations per calculation
operations = 0

# Accepts an position x as an integer. Calculates the 
# Fibonacci sequence up to position x. Returns the
# Fibonacci number at position x.
def calcFib(x):
    global operations
    operations += 1

    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return calcFib(x - 1) + calcFib(x - 2)

try:
    while True:
        position = input('Enter the fib you want to calc: ')
        val = int(position)
        print('#: ' + str(calcFib(val)))
        print('# of operations: ' + str(operations))
        operations = 0 # resets operation count for a new operation

except ValueError:
    pass # input was not a valid integer 