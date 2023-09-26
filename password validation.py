# password validation

password = 'nitin@123'

while 1:
    user_pass = input ('Enter the password')
    if user_pass == password:
        print('Login Succesfull')
        break
    else:
        print('Wrong password, Try Again')
