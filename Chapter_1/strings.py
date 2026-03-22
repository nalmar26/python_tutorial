variable1 = 'Initialize with Single Quote'
variable2 = "Initialize with Double Quotes"

print(variable1)
print(variable2)
print(type(variable1))
print(type(variable2))
print("Upper: ",variable1.upper())
print("Lower: ", variable2.lower())

brand = "x"
price = 999
tax=8.25
message = "The price of " + brand + " is $" + str(price) + ", and with tax of " + str(tax) + "% , it is " + str(price + (price*tax/100))
print(message)
format_message_with_percentage = "The price of %s is %2.2f, and with tax of %2.2f%% , it is %4.2f" %(brand,price,tax,(price + (price*tax/100)))
print(format_message_with_percentage)
print("The price of %s is %10.5f, and with tax of %2.2f%% , it is %15.9f" %(brand,price,tax,(price + (price*tax/100))))
format_message = "The price of {0:} is ${1:}, and with tax of {2:}% , it is {3:4.5f}".format(brand,price,tax,price + (price*tax/100))
print(format_message)
f_string_message = f"The price of {brand} is ${price}, and with tax of {tax}% , it is {price + (price*tax/100)}"
print(f_string_message)

'''result
$ python3 strings.py
Initialize with Single Quote
Initialize with Double Quotes
<class 'str'>
<class 'str'>
Upper:  INITIALIZE WITH SINGLE QUOTE
Lower:  initialize with double quotes
The price of x is $999, and with tax of 8.25% , it is 1081.4175
The price of x is 999.00, and with tax of 8.25% , it is 1081.42
The price of x is  999.00000, and with tax of 8.25% , it is  1081.417500000
The price of x is $999, and with tax of 8.25% , it is 1081.41750
The price of x is $999, and with tax of 8.25% , it is 1081.4175
'''