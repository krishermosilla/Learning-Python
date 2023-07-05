# they don't allow duplicates keys. It must be different, 
# but incase there is duplicates, it will not print the two keys, 
# only the most recent one.
# Example: 'name' - it a key while 'gem' is a value of the key.


my_dictionaries = {
    'Name': 'Gem',
    'Gender': 'Male',
    'Age': 19, # When you have a integer value, it does not have a problem at all.
    'Address':'Sabang', 
    'My_boyfriend': True,  
    'Girlfriend': ['Krisha', 'Ann', 'Olivar', 'Hermosilla'] # List can be also used in dictionaries
}
print(my_dictionaries['Girlfriend']) #You can print all the keys one by one
print(type(my_dictionaries)) # print what type of data.
print(len(my_dictionaries)) # to know how many dictionaries keys are stored.

x = my_dictionaries['Name'] # this is optional if you want to put a variable or representation.
print(x)

