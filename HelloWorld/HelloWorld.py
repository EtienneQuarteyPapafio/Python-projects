print('Hello world works with single \nor double quotes')
print()
# Hashtages are for making comments!
# with python there is no need to declare variable types

#strings can be combined with +, but use ' ' to space them out

first_name=input("Enter first name: ")
second_name=input("Enter second name: ")
full_name=(first_name +' '+ second_name)
print(full_name)
#strings can be modified with functions
print(full_name.upper()) #All Caps
print(full_name.lower()) #All lowercase
print(full_name.capitalize()) #Capitalized
print(full_name.count('e')) #how many of letter