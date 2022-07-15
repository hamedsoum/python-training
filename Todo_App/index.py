from hashlib import new
from user import user

todoList = list()
todo_dist = {}

def showInformation(firstName, lastName,age):
    print('firstName : ' + firstName )
    print('lastName : ' + lastName )
    print('age : ' + age )

def logIn(userName,password):
    print('user '+userName+ 'created successfully :')
    print('login now')
    loginUsername = input('Enter your login :')
    loginPassword = input('Enter your password :')

    if userName == loginUsername or password == loginPassword :
        print('User logged successfully')
    else :
        print('User logged failed')


print('welcome to the todo App! ')

print('let\'s start with a creation of you account ')

firstName = input('what is your firstName ?')
lastName = input('lastName :')
userName = input('userName :')
age = input('age :')
password = input('password : ')

print('you information')

showInformation(firstName, lastName,age)


informationCheck = input('confirm information? (1 for yes and 0 for no)')

if int(informationCheck) == 1 :
   logIn(userName,password)
else :
    print('information incorect')


