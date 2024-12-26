#Email Validator

import re
pattern='[a-z 0-9]+[._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

user_id = input("Enter Email id:")

if re.search(pattern,user_id):
     print('Email id is valid')    
else:
     print('Email id is invalid')