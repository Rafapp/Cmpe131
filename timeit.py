import time

def calculate_time(func):
    def wrapper():
        time_init = time.time()
        func()
        time_fin = time.time()
        print (f'Total time {str(time_fin - time_init)}')
    return wrapper

def solution():
    return

solution = calculate_time(solution)

solution()
