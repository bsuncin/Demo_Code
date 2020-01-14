# The goal of this program is to continue improvements from
# the Mem solution. It keeps its linear time and provides a
# work around for the stack limit problem by converting the
# recursive section into a for loop.

#tracks the operations per calculation
operations = 0

#saves results of previous calculations
table = {0 : 0, 1 : 1}

#Accepts an position x as an integer. Calculates the 
#Fibonacci sequence up to position x.
#Is a helper function to calcFib().
def calc(x):
    global operations, table
    
    lastPosition = len(table) - 1

    for i in range(lastPosition, x + 1):
        operations += 1
        table[i + 1] = table[i] + table[i - 1]

#Accepts an position x as an integer. Returns
# the Fibonacci number at position x. 
def calcFib(x):
    global table

    if x not in table:
        calc(x)
    
    return table[x]

try:
    while True:
        position = input('Enter the fib you want to calc: ')
        val = int(position)
        print('#: ' + str(calcFib(val)))
        print('# of operations: ' + str(operations))
        operations = 0 #resets operation count for a new operation

except ValueError:
    pass #input was not a valid integer