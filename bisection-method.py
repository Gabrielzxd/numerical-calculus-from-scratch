# Example function
def function(x):
    return x**3 - 9*x + 3

# Implementation using recursion
def bisection_method_recursive(function, a, b, error):
    x = (a + b) / 2

    if abs(function(x)) < error:
       return x
    
    if function(a)*function(x) < 0:
        return bisection_method_recursive(function, a, x, error)
    
    elif function(x)*function(b) < 0:
        return bisection_method_recursive(function, x, b, error)
    
    else:
        return -999999999

# Similar to binary search
def bisection_method_iterative(function, a, b, error):
    x = (a + b) / 2
    while abs(function(x)) > error:
        if function(a) * function(x) < 0:
            b = x
        if function(x) * function(b) < 0:
            a = x
        x = (a + b) / 2
    return x

# Test
x = bisection_method_recursive(function, 1, 3, 0.01)
print(x)
y = bisection_method_iterative(function, 1, 3, 0.01)
print(y)
