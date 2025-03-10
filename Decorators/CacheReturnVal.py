import time

def cache(fun):
    cache_val={}
    print(cache_val)
    def wrapper(*args,**kwargs):
        if args in cache_val:
            return cache_val[args]
        result=fun(*args,**kwargs)
        cache_val[args]=result
        return result
    return wrapper    

@cache
def long_running_fun(a,b):
    time.sleep(4)
    return a+b

print(long_running_fun(2,3))
print(long_running_fun(2,3))
print(long_running_fun(2,4))