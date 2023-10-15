name ='Ehsun'
print('Hello '+ name +' would you like to learn some Python today?')

print(name.lower())
print(name.upper())
print(name.title())

famous_message=('\tAlbert Einstein once said, " A person who never made a \n\t mistake never tried anythinng new."')
message=famous_message
print(message)

hello=(' Hello '.rstrip())
print(hello)
print(' Hello '.lstrip())
print(hello.lstrip())
print(' Hello '.strip())

print(3+5)
print(9-1)
print(2*4)
print(16/2)

favourite_number='4'
print('My favourite number is '+ favourite_number)

names=['Ehsun' ,'Sunny', 'Mano']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
print(names)
for variablename in names:
    print(variablename)

for name in names:
    print(f"{name.title()}, that was a great trick!")

message = f"My first friend was {names[0]}"
print(message)

pizzas=['veggie', 'chicken', 'mushroom']
for pizza in pizzas:
    print("I like "+ pizza)
print("I really love pizza")

counting=[]
for value in range(1,11):
  #  counting=value**3
    print(value)

PTI=['Imran Khan', 'Asad Umer','Shah Mahmmood', 'Miandad','Jahangir Khan', 'Elan Musk','Jeff Bez']
print('The first three items in the list are ' , PTI[0:3])
print('The items in the middle of the list are ', PTI[3:5])

friend_PTI=PTI[:]
PTI.append('appended item')
friend_PTI.append('appended item to the frinds list')
print('My favourite persons are')
for person in PTI:
    print(person)
print('My favourite persons are in the friend_PTI list are')
for person in friend_PTI:
    print(person)


food=('soup','noodle')
for value in food:
    print(value)

food = ('chicken','meat')
print("\nNew Value of food")
for values in food:
    print(values)


