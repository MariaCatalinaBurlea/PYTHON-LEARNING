variable = input("Add a number:\n")
my_list = [1, 2, 3]

try:
    if variable.isdigit():
        raise ValueError
    print(my_list[3])
    print(a)
    variable = int(variable)
except ValueError:
    print("value error exception")
    if variable.isdigit():
        variable = int(variable)
    a = None
except NameError:
    print("undefined variable")
    a = None
except IndexError:
    print("index error")
except Exception:
    print("default exception")
else:
    print("no exception was caught")
finally:
    print("it is run anyway")

print('variable', variable)
print('a', a)
