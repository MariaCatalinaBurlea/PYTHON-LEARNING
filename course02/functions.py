def empty_function():
    pass


empty_function()


def function_without_parameters():
    return "Ana are mere"


print(function_without_parameters())


def function_with_parameters(param_1=3, param_2=4):
    return param_1 + param_2


print(function_with_parameters(2, 3))
print(function_with_parameters(100))    # default value for param_2 is used


"""
*args -> as many parameters as we want 
        ->  CANNOT NAME THEM

**kwargs -> ALWAYS AFTER *args
"""


def function_with_args(param_1, param_2, *args, **kwargs):
    print(type(args))       # tuple
    print(type(kwargs))     # dictionary
    sum_of_args = param_1 + param_2
    for i in args:
        sum_of_args += i
    for i in kwargs.values():
        sum_of_args += i
    return sum_of_args


print(function_with_args(1, 2, 3, 4, 5, param_1=3, c=6))
