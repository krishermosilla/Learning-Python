a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
op = input('Enter an operator:')

#Operation: [Addition, Subtraction, Multiplication, Division]

if op == 'addition':
    print('The sum of', a, 'and', b, 'is', a + b ,'.')
    
elif op == 'subtraction':
    print('The difference of', a, 'and', b, 'is', a - b ,'.')
    
elif op == 'multiplication':
    print('The product of', a, 'and', b, 'is', a * b ,'.')
    
elif op == 'division':
    print('The quotient of', a, 'and', b, 'is', a / b ,'.')
else:
    print('Operation invalid.')