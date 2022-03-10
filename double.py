def doubler(func):
    def wrapper():
        func()
        func()
    return wrapper

@doubler
def solution():
    print('a print')

solution()



