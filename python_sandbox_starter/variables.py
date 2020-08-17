# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1 # int by default
y = 2.5 # float number
name = 'Benson' # str can be single or double quotes
do_again = True #bool 

# Multiple assignments
x, y, do_again = (1, 2.5, 'Benson', True)

# Basic Math 
a = x + y

print(type(x))

#casting 
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)




