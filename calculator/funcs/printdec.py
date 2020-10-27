def print_log(func):

    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}{args}{kwargs if kwargs else ""} = {result}')
        return result
    return inner





