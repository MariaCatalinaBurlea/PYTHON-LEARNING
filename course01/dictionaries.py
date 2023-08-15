# dictionary = {"key": "value", "key": "3"} -> it will change the value to key to 3 (with the last one)
dictionary = {"key": "value", "key1": "3"}
print(dictionary)
# print(dictionary['key2'])
print(dictionary['key1'])
print(dictionary.get('key2'))
print(dictionary.get('key2', 5))

# Add item
print("\nAdd item")
dictionary['key2'] = 5
dictionary.update({'key2': 5, 'key3': 6})
dictionary.update({'key1': 5})
print(dictionary)

# Get all keys, values
print("\nKeys + values + items")
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

# Remove keys
print("\nRemove")
dictionary.pop('key2')
print(dictionary)

dictionary.popitem()
print(dictionary)


