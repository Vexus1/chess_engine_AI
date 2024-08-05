from time import perf_counter

import matplotlib.pyplot as plt

GAMES_PLAYED = 100
games_time = []

# here should be class for multiple decorators
def time_multiple_games(func):
    '''Decorator that mesures time taken by AI for multilple games'''
    def wrapper(*args, **kwargs):
        for _ in range(GAMES_PLAYED):
            start_time = perf_counter()
            result = func(*args, **kwargs)
            end_time = perf_counter()
            time_passed = end_time - start_time
            games_time.append(time_passed)
        return result
    return wrapper
