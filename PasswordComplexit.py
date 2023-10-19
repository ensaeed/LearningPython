import re

def passwordComplexity(password):
    #passwordText=input('Enter the password: ')
    print('Have you entered the password')

    eightcharregex=re.compile (r'(\D){8,}')
    isDigitegex=re.compile(r'[0-9]+')
    isCharregex=re.compile(r'[a-zA-Z]+')
    specialregex=re.compile(r'[+*&%$£]+')
    if len(password)<=8:
   # if eightcharregex.findall(password)==[]:
        print('The password must be equal to 8 character')
    elif isDigitegex.findall(password)==[]:
        print('Please enter atleast 1 digit')
    elif isCharregex.findall(password)==[]:
        print('Please enter atleast one character')
    elif specialregex.findall(password)==[]:
        print('The password must contain special characters')
    else:
        print('Thanks for entering the pasword')
    return

passwordComplexity('1&23w456789')
