import time
from functools import wraps

def logtime(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Entering function: {func.__name__}')
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        print(f'Exiting function: {func.__name__}')
        print(f'{func.__name__} took {et - st} seconds')

        return result 
    return wrapper