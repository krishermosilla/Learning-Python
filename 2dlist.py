#2 dimensional lists

my_list = [1, 2, 3,4]
print(my_list) # this will print just a normal list

# but if we want tomak eit 2D list

my_numbers = [
    [0, 9, 2, 1], 
    [9, 3, 3, 6],
    [1, 2, 4]
 ]
print(my_numbers)

print('-------------------------------')
#when we want to get the value by using index number

print(my_numbers[1][0]) # the 1 represents the index number based on brackets/list and 
#0 is based on the index number from the index of the list, you can it anytime.add()

print('-------------------------------')
#Nested Forloops

for lists in my_numbers:
    print(my_numbers)
    
print('-------------------------------')

#when you want to  print the values in rows
for lists in my_numbers:
    for row in lists:
     print(row)
    