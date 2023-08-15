# myList = []
# print(type(myList))
# myList.append(3)
# myList.append(4)
# myList.append(3)
# myList.append("string")
# print(myList)

myList = [3, 4, 3, [1, '2', "element"], "string", "characters", "python"]
print(len(myList))
print(myList[3])
# list with fixed index -> print(myList[5])
# list with slice: list[start:end] -> takes the element from position start until end-1 position
# print(myList[2:5])
# print(myList[5:6])
# print(myList[0:6])
# print(myList[0:3])
# list with slice and step -> list[start:end:step]
print(myList[0:5:2])

# list[start:] -> the list from the start position
print(myList[0:])
print(myList[1:])

# list[:end] -> the list until end-1 position
print(myList[:4])

# myList[position][positionInInnerList] -> get the elem from the list which is inside of list
print(myList[3][2])

# myList[position][positionInInnerList][index] -> get the character from index from the inner list located in myList
print(myList[3][2][2])
# print(myList[3][2][7]) -> index out of range
print(myList[-4:-2])
print(myList[1:-3:2])

# INDEX
print("\nINDEX")
# index -> first occurrence in the list
print(myList.index(3))

# APPEND + INSERT
print("\nAppend + insert")
# append(elem -> add new element
myList.append(None)
print(myList)

# insert(index, elem) -> add elem on specific position/index
myList.insert(4, True)
print(myList)

# REMOVE + CLEAR + POP
print("\nRemove + clear + pop")
# remove(elem) -> removes elem
myList.remove(3)
print(myList)

# pop -> removes last elem
myList.pop()
print(myList)

# pop(index) -> removes the element from the specified index
myList.pop(3)
print(myList)

# clear -> removes all elements
myList.clear()
print(myList)

# COPY
print("\nCopy + list")

# copy -> copies a list into another one (shallow copy)
second_list = [False, "chemestry", 20.5]
copy_list = second_list.copy()
print(copy_list)

# list -> copy a list into another one
new_list = list(second_list)
print(new_list)

# REVERSE -> reverse a list
second_list.reverse()
print("\nReverse list: {}".format(second_list))

# SORT -> sort a list
first_list = [23, -54, 243, -200, 2384329, 243, -4394, 243]
first_list.sort()
print("\nSorted list: {}".format(first_list))

# COUNT -> counts the no of times an element appears in the list
print("\nCount: {}".format(first_list.count(243)))

# CONCATENATION
# using +
print("\nConcatenation using '+' and extend()")
third_list = first_list + second_list
print(third_list)

# extend
first_list.extend(third_list)
print(first_list)








