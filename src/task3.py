def decorator_3(f):                             
    counter = 0
    def inner_func(*args,**kwargs):  
                
        nonlocal counter
        counter += 1
        with contextlib.redirect_stdout(io.StringIO()) as fun:
            start = perf_counter()
            f(*args,**kwargs)
            end = perf_counter()
            time = end-start
        out = fun.getvalue()

        global ExeTimeDic
        ExeTimeDic[func.__name__] = time

        if len(ExeTimeDic.keys()) == 4:
           sort_time = sorted(ExeTimeDic.values())
           reverse = dict((v,k) for k,v in ExeTimeDic.items())
           table = [[reverse[s_f[0]],1,s_f[0]],[reverse[s_f[1]],2,s_f[1]],[reverse[s_f[2]],3,s_f[2]],[reverse[s_f[3]],4,s_f[3]]]
           print(tabulate(table, headers=["PROGRAM","RANK","TIME ELAPSED"]))
        else:
           pass
        file= open(f.__name__ + ".txt","w+")
        file.write( f'{func.__name__} has been called {counter} times and the execution time was {time} \nDESCRIPTION:\nName :{func.__name__} \nType: {type(func)} \nSign:{inspect.signature(func)} \nArgs: positional {args} \nkey=worded {kwargs} \nDoc :{func.__doc__} \nSource:{inspect.getsource(func)} \nOutput:{out}') 
                
    return wrapper
