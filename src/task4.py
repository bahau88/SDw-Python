import contextlib 
import time, io
import inspect
from contextlib import 

def decorator_2(f):
    def wrapper(*args, **kwargs):
        wrapper.count+=1
    try:
        with contextlib.redirect_stdout(io.StringIO()) as f_:
            f(*args, **kwargs)
            start = perf_counter()
            end = perf_counter()
        out = f.getvalue()
        print(f"{f.__name__} call {wrapper.count} executed in {end-start} sec") + ' sec')
        print('Name: '+func.__name__)
        print('Type: '+str(type(func)))
        print('Sign: '+str(inspect.signature(func)))
        print('Args: ' + str(args['args']))
        print('Doc: '+str(func.__doc__))
        print('Source: '+str(inspect.getsource(func)))
        print('Outputs: ', s)
        print('function outputs: ', out,"\n")

    except Exception as e:
        with open('log.txt','a') as e:
                with redirect_stdout(e) as f:
                    print(datetime.datetime.now(), err)

        return wrapper
        
        
