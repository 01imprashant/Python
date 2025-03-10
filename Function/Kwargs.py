def print_kwargs(**kwargs):
    for key,val in kwargs.items():
        print(f"{key}:{val}")


# print(print_kwargs(Name="Saktiman"))
# print(print_kwargs(Name="Saktiman",power="lazer"))
print(print_kwargs(Name="Saktiman",power="lazer",enemy="Dr.Jackaal"))