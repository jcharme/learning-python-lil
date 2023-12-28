#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I am a function")

# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# TODO: function that returns a value
def cube(x):
    return x*x*x

# TODO: function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# TODO: function with variable number of arguments
#* Star indicates variable number, variable arg lists must be last
# Loops through all arguments passed to add them together
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


#*Functions can be passed to different functions
# func1() #prints correctly
# print(func1()) #this doesn't print, but the function does
# print(func1) #prints none

# func2(10, 20)
# print(func2(10, 20))
# print(cube(3))

# #* prints the return value of a function
# print(power(2))
# print(power(2,3))

# #* If arg names are provided, they don't have to be in a specified order
# print(power(x=3, num=2)) 

print(multi_add(4,5,10,4, 10))