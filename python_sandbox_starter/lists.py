# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1,2,3,4,5]
fruit = ['Apple', 'Orange', 'Grapes', 'Pears']
# use a constructor
numbers2 = list((1,2,3,4,5))

print (numbers, numbers2)

#Get value of fruit list 
print(fruit[1])

# Get length of list 
print (len(fruit))

# Append to list
fruit.append('Mango')

#Remove from lists
fruit.remove('Grapes')

# Insert into position
fruit.insert(2,'Watermelon')

#Remove from certain position
fruit.pop(2)

# Reverse the lists 
fruit.reverse()

#Sort list
fruit.sort()



print(fruit)

