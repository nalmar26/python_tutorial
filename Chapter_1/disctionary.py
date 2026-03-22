myDict = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary: ", myDict)
print("Dictionary as string: ", str(myDict))
print("Dictionary type: ", type(myDict))
print("Value of 'name' key: ", myDict["name"])
print("Value of 'age' key: ", myDict["age"])
print("Value of 'city' key: ", myDict["city"])
myDict["country"] = "USA" # This will add a new key-value pair to the dictionary
print("Dictionary after adding 'country' key: ", myDict)
del myDict["age"] # This will delete the key-value pair with the key "age"
print("Dictionary after deleting 'age' key: ", myDict)