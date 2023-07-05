try:
    x = int(input('Input an integer: '))
    print(x)
except : #this will print if the input is error or not an integer
    print('Somethhing went wrong.... Please try again')
else: # this will print if the input is correct base on the data type
    print('Nothing went wrong..')
finally: #this will print whether it is an error or not
    print('try except finished') 