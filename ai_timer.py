from time import perf_counter

sum_time = []

def time_it(func):
    '''Decorator that measures the time taken by a function to execute.'''
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        time_passed = end_time - start_time
        print(f'Time taken for AI move: {time_passed:.4f} seconds')
        sum_time.append(time_passed)
        return result
    return wrapper
