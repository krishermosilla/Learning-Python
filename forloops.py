#"for" is the very firt word you will type in for loops.
#"letter" is jus a variable or representation, you can change it anytime.
#"Hello" is the string or value of the given variable.

for letter in 'I love you, Gem Felix!':
    print(letter)

print('-------------------------------')
    
# If you want to make it easier, just have a variable to represent.
#list can be used also.

myboyfriend = ['Gem', 'Felix', 'Otadoy']

a = myboyfriend
print(a)

print('-------------------------------')

#We will apply the dictionary
my_dictionaries = {
    'Name': 'Gem',
    'Gender': 'Male',
    'Age': 19, 
    'Address':'Sabang', 
    'My_boyfriend': True,  
    'Girlfriend': ['Krisha', 'Ann', 'Olivar', 'Hermosilla'] 
}

for values in my_dictionaries:
    print(values)
    
myhusband = ['Gem', 'Felix', 'Otadoy', 'hihi']

print('-------------------------------')

#If we want to stop in a certain value by using if statement and break

for values in myhusband:
    if values == 'Otadoy': #this means it will stop before the "otadoy"
        break
    print(values)
    
print('-------------------------------')
 
#But in this case, it will stop according to the condition
for values in myhusband:
    print(values)
    if values == 'Otadoy': #this means it will stop before the "otadoy"
        break
    
print('-------------------------------')

#range of numbers 

for x in range(5): #It depends of you value and it will start counting from 0, 0 as 1
    print(x)

print('-------------------------------')

#range of numbers with specific startinga nd stopping points
for y in range(3, 7): #it will start from 3, but it will stop before 7.
    print(y)


print('-------------------------------')

#range of numbers with else statements

for z in range(10):
    print(z)
else:
    print('Finishined Looping!!') #it will print after the looping