def decorated_div(fun):
    def wrapper(a,b):
        if b == 0:
            return "b is 0, it shouldn't be 0"
        else:
            return fun(a,b)
    return wrapper

@decorated_div
def div(a,b):
    return a/b

# Call the decorator with '@' or following method
#d = decorated_div(div)
#d(10,0)

div(10,0)
