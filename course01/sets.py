my_set = {1, 3, '5', 3, 4, 8}
print(my_set)    # 1, 3, '5'
print(type(my_set))
myList = [1, 2, 3, 4, 5, 3]
print(set(myList))
print(list(set(myList)))    # prints a list with unique elements due to set()

# print(mySet[1]) -> cannot access by index
print(list(my_set)[1])   # -> transform into list to access by index

# Remove + clear
print("\nRemove + discard + pop + clear")
my_set.remove(3)
print(my_set)
my_set.discard(4)
print(my_set)

# Union
my_second_set = {2, 3, 's', 45, 23, '5'}
my_second_set.union(my_set)
print(my_second_set)

# Update
my_third_set = {1, 2, 34, 56, -100}
my_second_set.update(my_third_set)


# Intersection
my_fourth_set = {-100, 20, 24, 25}
print(f"Intersection {my_second_set.intersection(my_fourth_set)}")

# isSubset
print(f"Subset: {my_third_set.issubset(my_second_set)}")

# isSuperset
print(f"Superset: {my_second_set.issuperset(my_third_set)}")