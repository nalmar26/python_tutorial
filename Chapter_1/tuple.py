tup = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
print("Tuple: ", tup)
print("Tuple as string: ", str(tup))
print("Tuple type: ", type(tup))
print("First month: ", tup[0])
print("Last month: ", tup[-1])
print("Subtuple of months from index 0 to index 3 (4 is exclusive): ", tup[0:4]) # from index 0 to index 3 (4 is exclusive
tup = tup + ("Holiday",) # This will concatenate the tuple with another tuple containing the string "Holiday"
print("Tuple after concatenation: ", tup)
print("Subtuple of months from index 0 to index 4 with step of 2: ", tup[0:5:2]) # from index 0 to index 4 (5 is exclusive) with step of 2, so it will take index 0, index 2, index 4, etc.
print("Tuple : ", tup)
#del tup[0] # This will throw an error because tuples are immutable and cannot be modified after they are created
del tup # This will delete the tuple
#print("Tuple : ", tup) # This will throw an error because the tuple has been deleted and cannot be accessed anymore