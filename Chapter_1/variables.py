sampleVariable = 10
sample_variable = 10
this_is_another_sample_variable = "variable value"
_this_can_be_another_variable = 10.009
#2_invalid_variable = "this will throw an error"
print(sample_variable, sampleVariable, this_is_another_sample_variable, _this_can_be_another_variable)

#multiple variables in single line
multi_var1, multi_var2 = 10, "variable2 value"

#print("multi_var1: " + multi_var1 +", multi_var2: "+ multi_var2) not works
print("multi_var1: " + str(multi_var1) +", multi_var2: "+ multi_var2)

#Assigning varaibles
multi_var1 = multi_var2

print("multi_var1: " + multi_var1 +", multi_var2: "+ multi_var2)