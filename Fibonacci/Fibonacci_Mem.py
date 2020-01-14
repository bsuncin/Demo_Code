# The goal of this program is to show an improvement
# to linear time from the recursive solution.
# It also shows a flaw in that it disregards stack limits. 

# tracks the operations per calculation
operations = 0

# saves results of previous calculations
table = {0 : 0, 1 : 1}

# Accepts an position x as an integer. Calculates the 
# Fibonacci sequence up to position x. Returns the
# Fibonacci number at position x.
def calcFib(x):
    global operations, table
    operations += 1

    if x not in table :
        table[x] = calcFib(x - 1) + calcFib(x - 2)
    
    return table[x]

try:
    while True:
        position = input('Enter the fib you want to calc: ')
        val = int(position)
        print('#: ' + str(calcFib(val)))
        print('# of operations: ' + str(operations))
        operations = 0 # resets operation count for a new operation

except ValueError:
    pass # input was not a valid integer