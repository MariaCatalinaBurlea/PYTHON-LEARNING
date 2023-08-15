first_variable = 1
second_variable = 2
message = "The first variable is smaller than the second one"
# Method 1
if first_variable == second_variable:
    print("They are equal")
elif first_variable > second_variable:
    print("The first variable is bigger than the second one")
else:
    print("The first variable is smaller than the second one")

# Method 2
if first_variable == second_variable:
    print("They are equal")
elif first_variable > second_variable:
    print("The first variable is bigger than the second one")
print(message)

# Ternary operator - a single condition
message = "They are equal" if first_variable == second_variable else "The first variable is smaller than the second one"
print(message)

# Assignation in if
if (message1 := "They are equal") and first_variable == second_variable:
    message = message1
print(message1)

# The assignation will not take place since the first cond is false
if first_variable == second_variable and (message2 := "They are equal"):
    message = message2
print(message2)
