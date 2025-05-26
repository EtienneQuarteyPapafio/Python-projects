
#For easier formatting longer strings you can use the .format function

first_name='Jack'
last_name='Jones'
output='Hello, {} {}'.format(first_name, last_name)

#The curly brace are placeholders based on the order 
#we specify for first output
#or the second way with 0 and 1 for reusing elsewhere
output='Hello, {0} {1}'.format(first_name, last_name)

#in python three you can use f at the begginning for easy formatting

output=f'Hello, {first_name} {last_name}'



