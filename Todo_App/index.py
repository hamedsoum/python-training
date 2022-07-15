from hashlib import new
from user import user

todoList = list()
todo_dist = {}
logged = False
firstName = ''
lastName = ''
userName = ''
age = 0
password = ''

def welcome():
    print('welcome to the todo App! ')
    print('let\'s start with a creation of you account ')



def createUser(first : str,last:str,user:str,age: int,password: str):
    first = input('what is your firstName ?  ' )
    lastName = input('lastName :')
    userName = input('userName :')
    age = int(input('age :'))
    password = input('password : ')



def showInformation(firstName, lastName,age):
    print('firstName : ' + firstName )
    print('lastName : ' + lastName )
    print('age : ', age )
    print('you information')
    informationCheck = input('confirm information? (1 for yes and 0 for no)')
    if int(informationCheck) == 1 :
        logIn(userName,password)
        actionsToMake()
    else :
        print('information incorect')


def logIn(userName,password):
    print('user '+userName+ 'created successfully :')
    print('login now')
    loginUsername = input('Enter your login :')
    loginPassword = input('Enter your password :')
    if userName == loginUsername or password == loginPassword :
        print('User logged successfully')
        logged = True
    else :
        print('User logged failed')
 


def actionsToMake():
    if logged == True :
        action = input('what do you want to do? 1 for list all to-dos or 2 for add a new to-do ')
        if int(action) == 1 :
            print(todoList)
        elif int(action) == 2 :
            expense = input('expense :') 
            expenseAmount = input('amount :' ) 
            todo_dist = {
                'expense' : expense,
                'expenseAmount' : expenseAmount
            }
            todoList.append(todo_dist)
            for todo in todoList :
                 print(todo)
    else :
        print('vous devez vous connecter avant de continuer')

welcome()
createUser(firstName,lastName,userName,age,password )
showInformation(firstName, lastName,age)
logIn(userName,password)
actionsToMake()





