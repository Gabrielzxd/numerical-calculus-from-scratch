# Example function
def function(x):
    return x**3 - 9*x + 3

# Implementation using recursion
def bisection_method_recursive(function, a, b, error):
    if (function(a) * function(b) >= 0):
        return -999999999
    x = (a + b) / 2

    if abs(function(x)) < error:
       return x
    
    if function(a)*function(x) < 0:
        return bisection_method_recursive(function, a, x, error)
    
    if function(x)*function(b) < 0:
        return bisection_method_recursive(function, x, b, error)


# Similar to binary search
def bisection_method_iterative(function, a, b, error):
    if(function(a) * function(b) < 0):
        x = (a + b) / 2
        while abs(function(x)) > error:
            if function(a) * function(x) < 0:
                b = x
            if function(x) * function(b) < 0:
                a = x
            x = (a + b) / 2
        return x
    return -999999999

# Test
x = bisection_method_recursive(function, 1, 3, 0.01)
print(x)
y = bisection_method_iterative(function, 1, 3, 0.01)
print(y)
