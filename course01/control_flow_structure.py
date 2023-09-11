# While statement
while True:
    print("Set of instructions")
    break

first_variable = 1
second_variable = 2
while first_variable < second_variable:
    print(second_variable, 'line 9')
    first_variable += 1
else:
    print(second_variable, 'line 12')

# For statement
for i in "Anne has apples":
    print(i)

# For using enumerate
for i, v in enumerate("Anne has apples"):
    print(i, v)

my_list = ['shopping', 'reading']
for i, v in enumerate(my_list):
    print(i)

# For using range(end), range(start, end), range(start,end, step)
# It will go until end-1

for i in range(10):
    print(i)

for i in range(3, 10):
    print(i)

for i in range(3, 10, 3):
    print(i)

# For in dictionary
dictionary = {"book1": 1, "book2": 2, "book3": 3}
for i in dictionary:
    print(i)

# Using .keys()
for i in dictionary.keys():
    print(i)

# Using .values()
for i in dictionary.values():
    print(i)

# Using .items()
for i in dictionary.items():
    print(i)    # tuples

for i, v in dictionary.items():
    print(i, v)

# Each element of the tuple is put in a variable
# The same as the one with i,v in dictionary.items()
for i in dictionary.items():
    index, value = i
    print(index, value)

# break
import random

while True:
    random_choice = random.choice([1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    if random_choice % 3 == 0:
        break
    print(f"the choice was: {random_choice}")

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"odd number {i}")

# pass - placeholder role, in order to fill a block with instructions
if True:
    pass

