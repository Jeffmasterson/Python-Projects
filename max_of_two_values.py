#Jeff Masterson
#Chapter 5 #12


def function_max(value1, value2):
    if value1 > value2:
        return value1
    else:
        return value2
# get the two integer values
value1 = input("Please enter first integer value: ")
value2 = input("Please enter second integer value: ")

# call the function
max_value = function_max(value1, value2)

# show the result
print ('Max value = ', max_value)



