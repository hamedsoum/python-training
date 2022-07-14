# boy = True
# short = False

# if boy == True and short == False :
#     print('he is a boy or he is short')
# else :
#     print('A is none of rhe two')

value = input('Input a value: ')

if type(value) == str:
    print(value + ' is a string')
elif type(value) == int:
    print(value + ' is an integer')
elif type(value) == list :
    print(value + ' is a list')
else :
    print('we don\'t know the data type of ' + value)
