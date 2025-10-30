# Example function
def function(x):
    return x**3 - 9*x + 3

def method_false_position_recursive(function, a, b, error):
    if function(a) * function(b) >= 0:
        return -999999999
    
    x = (a * function(b) - b * function(a))/(function(b) - function(a))

    if abs(function(x)) < error:
       return x
    
    if function(a)*function(x) < 0:
        return method_false_position_recursive(function, a, x, error)
    
    if function(x)*function(b) < 0:
        return method_false_position_recursive(function, x, b, error)

# Implementation iterative method 
def method_false_position_iterative(function, a, b, error):
    if(function(a) * function(b) < 0):
        x = (a * function(b) - b * function(a))/(function(b) - function(a))
        while abs(function(x)) > error:
            if function(a) * function(x) < 0:
                b = x
            if function(x) * function(b) < 0:
                a = x
            x = (a * function(b) - b * function(a))/(function(b) - function(a))
        return x
    return -999999999


# Test
x = method_false_position_recursive(function, 1, 3, 0.01)
print(x)
y = method_false_position_iterative(function, 1, 3, 0.01)
print(y)