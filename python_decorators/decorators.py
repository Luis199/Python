# def printfib():
#     '''print out fibonacci'''
#     print('Fibonacci')


# print(type(printfib()))

def my_decorator(func):
    '''Decorator Function '''

    def wrapper():
        return "F-I-B-O-N-A-C-C-I"
    return wrapper


@my_decorator
def  pfib():
    return "Fibonacci"

print(pfib)