#if you want to make put many names
def greetings_function(*names):
    print('Welcome ' + names[1])
    
greetings_function('Gem', 'Krisha', 'Reygine')

#
def greetings_function(name, age):
    print('My name is '+ name+ '.' + ' I am ' + str(age) + ' years old.')
    
name =  input('Enter your name:')
age = input('Enter your age:')
greetings_function(name, age)