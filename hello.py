'''
Learning Python
By Chris Chike
2019

'''

import os
os.system('clear')
'''
full_name = "christian ubani"
full_name = "chris ubani"
age = 0  # number data types
names = ["john", "Mike", "Mary"]
print("hi")
# printing here i come to the screen this is the programatic
print(full_name)
print(names)
'''
####
# Strings
####

name = "My name is chris chike chris"

# print(name)
print(len(name))
print(name.split(" "))
print(name.split(" ")[2:4])

'''
Numbers
'''
num = 100

print(float(num))

# Lists

# create list
my_colors = ['blue', 'red', 'purple', 'orange']

# add
my_colors.append('black')  # adds to the end
print(my_colors)
my_colors.insert(3, 'ash')  # inserts at position index 3
print(my_colors)
# remove vs pop vs del
my_colors.remove('blue')
print(my_colors)
my_colors.pop()  # takes out the last item
del my_colors[2]
print(my_colors)

# traverse
for color in range(0, len(my_colors)):
    print(my_colors[color])
names = ["john", "micah", "mandy"]


pri_color = my_colors[:2]
print(pri_color)
