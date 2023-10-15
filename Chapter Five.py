alien_colour='blue'
if alien_colour=='green':
    print('yes the colour is green')
elif alien_colour=='yellow':
    print('You have earned 10 points')
elif alien_colour=='red':
    print('You have earned 15 points')
else:
    print('no the colour is not green')

age=65
if age==1:
    print("Person is a baby")
elif age>=2 and age<4:
    print("Person is a toddler")
elif age>=4 and age<13:
    print('Person is a kid')
elif age>=13 and age<20:
    print('Person is a teenager')
elif age>=20 and age<60:
    print('Person is an adult')
else:
    print('Person is an elder')

favourite_fruits=['apple','orange','kiwi']
for fruit in favourite_fruits:
    if fruit=='apple':
        print('you readlly like apple')
    elif fruit=='orange':
        print('you really like orange')
    elif fruit=='kiwi':
        print('You really like kiwi ')
    else: print('Your fruite is not in the list')


usernames=[]
#for username in usernames:
if usernames:
    print('We need to find some users')

else:
    print('We need to find some users')
'''elif usernames=='admin':
        print('Hello admin, would you like to see a status report')
elif usernames=='Ehsun':

        print('Hello Ehsun, thank you logging again')
elif usernames=='user1':
        print('Hello user1 thank you for logging again')
elif username=='user2':
        print('Hello user2 thank you for logging again')
elif username=='user3':
        print('Hello user2 thank you for logging again')
'''
current_users=['ehsun1','admin', 'user1','user2','user3']

new_users=['EHSUN1','admin1', 'user1','user2','user3']

lower_case_users=current_users[:]
lower_case_users
for users in current_users:
    lower_case_users=users.lower()
   # print(lower_case_users)

for users in lower_case_users:
    if users in current_users:
        print(f"Please enter a new username as {users} is already taken")


for users in new_users:
    if users in current_users:
        print(f"Please enter a new username as {users} is already taken")
    else:
     print(f"This user {users} is available")


print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

num=[1,2,3,4,5,6,7,8,9,10]
for numbers in num:
    if numbers==1:
        print("1st")
    elif numbers==2:
        print("2nd")
    elif numbers==8:
        print("8th")
else:
    print("9th")