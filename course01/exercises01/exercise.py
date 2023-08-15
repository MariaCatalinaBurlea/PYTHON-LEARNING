# 1. Create a list with the following elements: 7, 8, 9, 2, 3, 1, 4, 10, 5, 6
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)

# 2. Print a sorted list (the initial list does not change)
# sorted_list = list(my_list)
sorted_list = my_list.copy()
sorted_list.sort()
print(sorted_list)

# 3. Print a descended sorted list (the initial list does not change)
sorted_descended_list = list(my_list)
sorted_descended_list.sort(reverse=True)
print(sorted_descended_list)

# 4. Print the even numbers from a list( using ONLY SLICE)
even_indices = [i for i, number in enumerate(my_list) if number % 2 == 0]
even_numbers = [my_list[i] for i in even_indices]
print(even_numbers)

# 5. Print the odd numbers from a list (using ONLY SLICE)
odd_indices = [i for i, number in enumerate(my_list) if number % 2]
odd_numbers = [my_list[i] for i in odd_indices]
print(odd_numbers)

# 6. Print the numbers that are multiple of three
multiple_of_three_indices = [i for i, number in enumerate(my_list) if number % 3 == 0]
multiple_of_three_numbers = [my_list[i] for i in multiple_of_three_indices]
print(multiple_of_three_numbers)