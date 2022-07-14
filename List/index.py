# Creating a list of countries
# countries = list(('United kingdon', 2, True, 'Autralia'))

# name = 'Tomi'
# Printing the values in the list
# for value in countries :
#     print(value)

# Printing the first value in the list
# print(countries[0])

# Printing the values from index 1 to index 3
# print(countries[1:4])

# Printing the last value in the list
# print(countries[-1])

# Printing the length of the list
# print(len(countries))

# print(countries)


# --------------List method---------------------


list1 = [2,5,1,4,2]
list2 = ['banana', 'apples', 'mango', 'ornages', 'mango']

# list1.extend(list2)

# Adding the value 'cherry' to the list
list2.insert(1, 'cherry')

print(list2)

# It removes the value 'banana' from the list
# list2.remove('banana')

# print (len(list2))

print(list2.index('mango'))

print(list2.count('mango'))

# list2.clear()

# list2.remove('banana')

del list2[0]

print(list2)


list1.sort()

print(list1)

list3 = list2.copy()

print(list3)





