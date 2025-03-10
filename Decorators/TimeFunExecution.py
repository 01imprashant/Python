import time

def timer(fun):
    def wrapper(*arges,**kwargs):
        start=time.time()
        result=fun(*arges,**kwargs)
        end=time.time()
        print(f"{fun.__name__} run in {end-start}sec of time")
        return result
    return wrapper


@timer
def example_fun(n):
    time.sleep(n)

example_fun(2)    