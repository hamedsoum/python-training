# TUPPLE

# three_numbers = tuple((1, 2, 3, 1))
# strings = ('home', 'land', 'earth')
# boo = (True, False, True)
# print(three_numbers[0])


# FUNCTION

# def greetings_function(name, age) :
#     print('welcome' +name+ 'You are '+ str(age)+ ' years old. ')

# name = input('what is your name :')
# age = input('Enter your age: ')
# greetings_function(name, age)

# def callMyName (num1, num2) :
#     return num1 + num2

# print(callMyName(1,2))
# IF STATEMENT


# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# op = input('Enter Operator')

# if op == '+':
#     print('the addition is' , num1 + num2)
# elif op == "-" :
#     print('the substraction', num1 - num2)
# elif op == "*" :
#     print('the mutiplication', num1 * num2)
# elif op == "/" :
#     print('the division', num1 / num2)
# elif op == "%" :
#     print('the modulo', num1 % num2)
# else :
#     print('the operator not existing')

# TRY EXCEPT
# try:
#     x = int(input('Input an integer:'))
#     print(x)

# except :
#     print('Value not a integer')

# CLASS OBJET
# from new import Student

# class Person(Student):
#     pass

# p1 = Person()
# print(p1.name)


#--------------- WORK WITH FILE------------------

# It opens the file countries.txt in read mode.
# count_file = open('countries.txt', 'r')
# Checking if the file is readable.
# print(count_file.readable())

# Reading the first line of the file.
# print(count_file.readline())

# Reading all the lines in the file.
# print(count_file.readlines())

# Reading all the lines in the file.
# for line in count_file.readlines():
#     print(line)


# It opens the file countries.txt in write mode.
# count_file = open('newFile.txt', 'w')

count_file = open('new.py', 'a')


count_file.write('print(\'this is a new file\')')
# It closes the file.
count_file.close()
