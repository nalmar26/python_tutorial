print("int(10.5): ", int(10.5)) # This will convert the float 10.5 to the integer 10
print("float(10): ", float(10)) # This will convert the integer 10 to the float 10.0
print("str(10): ", str(10)) # This will convert the integer 10 to the string "10"
print("str(10.5): ", str(10.5)) # This will convert the float 10.5 to the string "10.5"
print("int(\"10\"): ", int("10")) # This will convert the string "10" to the integer 10
print("float(\"10.5\"): ", float("10.5")) # This will convert the string "10.5" to the float 10.5
print("str(10.5): ", str(10.5)) # This will convert the float 10.5 to the string "10.5"
#print(int("10.5")) # This will throw an error because "10.5" cannot be converted to an integer directly
print("int(float(\"10.5\")): ", int(float("10.5"))) # This will convert the string "10.5" to the float 10.5, and then to the integer 10
