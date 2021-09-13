def decorator_1(f):
# function decorator that calculate function execution time and the number of times the decorated function was called.
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        with contextlib.redirect_stdout(io.StringIO()) as _f:
            start = perf_counter()
            f(*args, **kwargs)
            end = perf_counter()
        print(f'{f.__name__} call {wrapper.count} executed in {end_time - start_time} sec')
    wrapper.count = 0
    return wrapper
