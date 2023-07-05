list1 = [2, 5, 3, 4, 1]
list2 = ['Jennie', 'Lisa', 'Rose', 'Jisoo']

#To add value on the list {use APPEND}
list1.append('6')
print(list1)

list2.append('V')
print(list2)
#To add a value to the list with a certain index number {use INSERT}
list1.insert(2, 10)
print(list1)

list2.insert(3,'Heeseung')
print(list2)


#To determine the number inside the list {use LEN}
print(len(list1))
print(len(list2))

#To remove a value to the list {use REMOVE}
list2.remove('Jennie')

#To print the index number of a certain value in the list {use INDEX}
print(list1.index(1))

#To count how many certain value in the list {use INDEX}
print(list1.count(1))

#To add a value to the list with a certain index number {use INSERT}
list1.insert(2, 10)
print(list1)

list2.insert(3,'Heeseung')
print(list2)

#To combine all the lists together {use EXTEND}
list1.extend(list2)
print(list1)


list1.clear()
print(list1)

list2.clear()
print(list2)




