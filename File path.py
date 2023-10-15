import os, shelve, pprint
from selenium import webdriver

webdriver

print(os.path.abspath('.'))
print(os.path.abspath('.\\File path.py'))

print(os.path.join('spam','usr'))
print(os.getcwd())
print(os.path.getsize('C:\\Users\\User\\PycharmProjects\\LearningPython'))
print('''''''''''''''''''''''''''''''''''')
totalsize=0
for filename in os.listdir(('C:\\Users\\User\\PycharmProjects\\LearningPython')):
    print(filename)
    totalsize=totalsize+os.path.getsize(filename)
print(totalsize)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
hellofile=open('C:\\Users\\User\\PycharmProjects\\LearningPython\\sonnet29.txt.txt')
hellocontent=hellofile.read()
#hellocontent=hellofile.readlines()
print(hellocontent)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
hellofile=open('C:\\Users\\User\\PycharmProjects\\LearningPython\\food.txt','w')
hellofile.write('Hello world!\n')
hellofile.close()
hellofile=open('C:\\Users\\User\\PycharmProjects\\LearningPython\\food.txt')
content=hellofile.read()

print(content)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
shelffile=shelve.open('mydata')
cats=['Zophie','Pooka','Simon']
shelffile['cats']=cats
shelffile.close()
shelffile=shelve.open('mydata')
print(list(shelffile.keys()))
print(list(shelffile.values()))
shelffile.close()
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
cats=[{'name':'zophine','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
print(pprint.pformat(cats))

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

file=open('C:\\Users\\User\\Downloads\\car_output.txt')
print(file.read())