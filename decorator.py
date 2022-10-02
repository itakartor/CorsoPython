def my_decorator (func):
    def decorator():
        return func()//2;
    return decorator();

@my_decorator
def sumPair():
    result = 2
    if(2%2 == 0 and 6%2 == 0):
        result = 2+6
    else:
        result = 3
    return result

print(sumPair)
