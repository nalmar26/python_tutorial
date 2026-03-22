userAge = [25, 30, 35, 40, 45]
print("User age list: ", userAge)
print("User age list as string: ", str(userAge))
print("User age list type: ", type(userAge))
print("First user age: ", userAge[0])
print("Last user age: ", userAge[-1])
print("sublist of user age: ", userAge[1:3])# from index 1 to index 2 (3 is exclusive) 1 to 3-1
userAge.append(50)
print("User age list after appending 50: ", userAge)
userAge[0] = 26
print("User age list after updating first element to 26: ", userAge)
userAge[-1] = 46
print("User age list after updating last element to 46: ", userAge)
print("sublist of user age after update 0 to 4 every second element: ", userAge[0:4:2])# from index 0 to index 3 (4 is exclusive) with step of 2, so it will take index 0 and index 2
print("sublist with default start and end: ", userAge[::2])# from index 0 to the end of the list with step of 2, so it will take index 0, index 2, index 4, etc.
print("sublist with default start : ", userAge[:3])# from index 0 to the end of the list with step of 3, so it will take index 0, index 3, index 6, etc.
print()
print("-" * 60)
print()
print("User age list: ", userAge)
del userAge[1] # This will delete the element at index 1 (which is 30)
print("User age list after deleting element at index 1: ", userAge)
del userAge[-1] # This will delete the last element (which is 46)
print("User age list after deleting last element: ", userAge)
del userAge[0:2] # This will delete the elements from index 0 to index 1 (2 is exclusive), so it will delete index 0 and index 1 (26 and 35)
print("User age list after deleting elements from index 0 to index 1: ", userAge)
userAge.append("50") # This will append the string "50" to the end of the list
print("User age list after appending string '50': ", userAge)
userAge.append("Hi How are you?") # This will append the string "Hi How are you?" to the end of the list
print("User age list after appending string 'Hi How are you?': ", userAge)
del userAge[-2] # This will delete the second last element (which is "50")
print("User age list after deleting second last element: ", userAge)