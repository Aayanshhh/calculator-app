def addition(A,B):
    return (A+B)

def subtraction(A,B):
    return (A-B)

def do_division(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return "Cannot divide by Zero"