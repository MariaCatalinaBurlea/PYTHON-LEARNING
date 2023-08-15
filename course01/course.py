# OPERATORS
# 1. Math operators
a = 3   # int
b = 3.4
c = 1j
# print(a)
# print(type(a))
# print(type(b))
# print(type(c))
# b = int(b)
print(type(b))
c = a / b
print(c)
c = a % b   # modulo
print(c)

# floor division operator -> in other languages is 'div'
# -> rounding down
c = a // b
print(c)

c = a ** b
print(c)

# 2. Comparison Operators
print(5 == 5)
print(5 != 5 and 4 > 3)

# 3. Logic Operators
"""AND
true and true => true
t and f => f
f and t => f
f and f => f
"""

"""OR
t or t => t
t or f => t
f or t => t
f or f => f
"""

# 4. Identity operators
# they are in the same memory location

# is -> used for objects,
#    -> used also with True print(7 is True)
# is not
# print(7 is 7)

# 5. Ownership operators
print(1 in [1, 2, 3])
print(1 not in [2, 4, 5])

# Variables
# Assign -> =
# Comparison -> ==
variable = 5
print(variable == 4)

a = 1
a += 1
print(a)
a -= 1
print(a)

# STRINGS
variable = 'Anne has "3" apples'
variable = "Anne has '3' apples"
variable = 'Anne has \'3\' apples'
apple_no = 3
pears_no = 4

# Method 1 - from Python 2
variable = "Anne has " + str(apple_no) + " apples"

# Method 2 - from Python 3
variable = "Anne has {} apples and {} pears".format(apple_no, pears_no)
variable = "Anne has {0} apples and {1} pears".format(apple_no, pears_no)
variable = "Anne has {1} apples and {0} pears".format(apple_no, pears_no)
print(variable)

# Method 3 - from Python 3.8
variable = f"Anne has {apple_no} apples and {pears_no} pears"


# Multiline string
print("\nMultiline string")
print("""Somnoroase pasarele
Pe la cuiburi se aduna
Se ascund in ramurele
Noapte buna""")

# Instead of using \n
print("\nSomnoroase pasarele\nPe la cuiburi se aduna")

# Raw string - to not perform escape to the escape character
print("\nRaw string")
print(r"Somnoase pasarele\nPe la cuiburi se aduna")

# Formatting
print("\nFormatting")
print("For only {price: .2f} dollars {cheers_msg}".format(price=49, cheers_msg="Have a great day!!"))
print("For onlu {0:.2f} dollars {1}".format(50, "Have a great day!"))
print("For only {:.2f} dollars {}".format(100, "Have a great day!"))
print("\nUsing F-strings(no need of placeholders):")
print(F'For only {49:.2f} dollars! {"Have a great day"}')
