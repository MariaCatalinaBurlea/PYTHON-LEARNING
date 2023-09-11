a = 2


def function():
    global message
    message = "Good evening"
    print(message)


function()
print(message)
# print(message)


# first_function => enclosing function
# second_function => enclosed function


def first_function():
    def second_function():
        print(f"Second function: {msg}")
    msg = "Good evening"
    second_function()
    print(f"New function: {msg}")


first_function()
