
def debug(fun):
    def wrapper(*args,**kwargs):
        args_val=", ".join(str(arg) for arg in args)
        kwargs_val=", ".join(f"{key}={val}" for key,val in kwargs.items())
        print(f"Calling:{fun.__name__} || with args: {args_val} and kwargs: {kwargs_val  }")
        return fun(*args,**kwargs)
    return wrapper    


@debug
def greet(name,greeting="Hello"):
    print(f"{greeting} {name }")

greet("Prashant")    