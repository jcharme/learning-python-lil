# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2} #* one and two are keys

# print(myint)
# print(myfloat)
# print(mystr)
# # print(mybool)
# # print(mylist)
# # print(mytuple)
# # print(mydict)

# # re-declaring a variable works
# myint = "abc"
# print(myint)

# # to access a member of a sequence type, use []
# print(mylist[2])
# print(mytuple[1])

# #* use slices to get parts of a sequence, the third is the step value
# print(mylist[1:5])
# print(mylist[1:5:2])

# #* you can use slices to reverse a sequence
# print(mylist[::-1]) #* Cool tip

# dictionaries are accessed via keys
#print(mydict["one"])

# ERROR: variables of different types cannot be combined
#print("string type " + str(123)) #* Cannot use different datatypes in same print statement, convert them

# Global vs. local variables in functions
def someFunction():
    global mystr
    mystr = "def" 
    print(mystr)

someFunction()
print(mystr) 

del mystr #* Deletes the variable (can undefine)
print(mystr)
