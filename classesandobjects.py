class Person: #the name of the class is the person
    def __init__(boy, name, age): #init means initialze and it should be between two underscores
        boy.name = name # the boy is tha parameter
        boy.age = age
name = input('Enter your name:')
age = input('Enter your age:')
p2 = Person(name, age)
print(p2.name)
print(p2.age)

