print('Create you account')
userName = input('Enter your username : ')
password = input('Enter your password : ')


print('user '+userName+ 'created successfully :')
print('login now')

loginUsername = input('Enter your login :')
loginPassword = input('Enter your password :')

if userName == loginPassword or password == loginPassword :
    print('User logged successfully')
else :
    print('User logged failed')
