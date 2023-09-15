# Ex 1: Function that computes the sum of the parameters (integers of real numbers)
# The function receives unknown numbers of parameters


def sum_of_parameters(*args, **kwargs):
    sum_of_args = 0
    for i in args:
        if isinstance(i, (int, float)):
            sum_of_args += i
    return sum_of_args


print("-> Exercise 1")
print(sum_of_parameters(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_of_parameters())
print(sum_of_parameters(2, 4, 'abc', param_1=2))


# Ex 2: Recursive functions that return
# 1. the sum of the numbers between [0, n]
def sum_of_n_numbers(n):
    if n == 0:
        return 0
    return sum_of_n_numbers(n-1) + n


# 2. sum of even numbers
def sum_of_even_numbers(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + sum_of_even_numbers(n - 2)
    return sum_of_even_numbers(n - 1)


# 3. sum of odd numbers
def sum_of_odd_numbers(n):
    if n == 1:
        return 1
    if n % 2:
        return n + sum_of_odd_numbers(n - 2)
    return sum_of_odd_numbers(n - 1)


print("\n-> Exercise 2")
print(f"Sum of the first 6 numbers: {sum_of_n_numbers(6)}")
print(f"Sum of even numbers: {sum_of_even_numbers(6)}")
print(f"Sum of odd numbers: {sum_of_odd_numbers(6)}")


# Ex 3: Function that reads from console and returns its value if it is an integer, else returns 0
def is_integer():
    variable = input("Enter an integer: ")
    if variable.isdigit():
        return variable
    return 0

print("\n->Exercise 3")
print(is_integer())