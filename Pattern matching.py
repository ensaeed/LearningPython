import re, webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from csv import writer
import difflib
import time
p

#phoneNukRegex contains the regex object
phoneNumRegex=re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found is:'+ mo.group())
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

numRegex=re.compile(r'^\d{1,3}?(,\d{3})*$')
mo=numRegex.search('1,234')
print(mo.group())
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxx')
nameRegex=re.compile(r'[A-Z][A-Z|a-z]*\sNakamoto')
mo=(nameRegex.search('Santoshi Nakamoto'))
print(mo.group())
print('--------------------------------------')

sentRegex=re.compile('[A|B|C][A-Za-z]+\s(eats|EATS|pets|throws)\s[A-Za-z]+\.')
print(sentRegex.search('Alice throws footballs.'))
#print(mo.group())
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
passwordRegex=re.compile(r'[a-zA-Z0-9._%-]{8,}?')
print(passwordRegex.search('gfdgfdgdfgh'))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
carRegex=re.compile(r'[A-Z0-9+]{7,8}|[A-Z\s0-9]{7,9}')
text=('There are multiple websites avaiable to check current car value in United Kingdom.The best of all is webuyanycar.com for intant valuation.The other examples are autotrader.com and confused.com.Checking example BMW with registration DN09HRM the value of the car is roughly around £3000.However car with registration  is not worth much in current market.There are multiple cars available higher than £10k with registraions KT17DLX and SG18 HTN.')
registrationnumbers=[]
#registrationnumbers=len(carRegex.findall(text)))
registrationnumbers=carRegex.findall(text)
print(registrationnumbers)
browser=webdriver.Firefox()
browser.get('https://www.carcheck.co.uk/')
#registation={}


file_name='CarDetails.csv'
with open(file_name, 'w',newline='', encoding='utf8') as f:
        f.write=csv.writer(f)
        f.write.writerow(['REGISTRATION', 'MAKE', 'MODEL', 'COLOR','YEAR'])

        for regnumber in registrationnumbers:
                browser.find_element(By.ID,'subForm').send_keys({regnumber})
                browser.find_element(By.TAG_NAME,'button').click()
                browser.implicitly_wait(10)
                print('Registration')
                print(regnumber)
                make=browser.find_element(By.XPATH,'//th[contains(text(),"Make")]')
                makeValue=browser.find_element(By.XPATH,'/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[1]')
                print(make.text)
                print(makeValue.text)
                model=browser.find_element(By.XPATH,'//th[contains(text(),"Model")]')
                modeValue=browser.find_element(By.XPATH,'/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[1]')
                print(model.text)
                print(modeValue.text)
                colour=browser.find_element(By.XPATH,'//th[contains(text(),"Colour")]')
                colourValue=browser.find_element(By.XPATH,'/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/table[1]/tbody[1]/tr[3]/td[1]')
                print(colour.text)
                print(colourValue.text)
                year=browser.find_element(By.XPATH,'//th[contains(text(),"Year of manufacture")]')
                yearValue=browser.find_element(By.XPATH,'/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/table[1]/tbody[1]/tr[4]/td[1]')
                print(year.text)
                print(yearValue.text)
               # registation.app
                registation = [regnumber, makeValue.text, modeValue.text, colourValue.text, yearValue.text]
                f.write.writerow(registation)
                browser.find_element(By.XPATH,'//header/div[1]/div[2]/a[1]').click()
                print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


browser.implicitly_wait(10)
browser.quit()


def comparefiles():
        originalFile=open('C:\\Users\\User\\Downloads\\car_output.txt').readlines()
        time.sleep(0.5)
        postFile=open('C:\\Users\\User\\PycharmProjects\\LearningPython\\CarDetails.csv').readlines()
        difference = difflib.HtmlDiff(wrapcolumn=800).make_file(originalFile,postFile)
        difference_report = open('./comparison.html', 'w+')
        difference_report.write(difference)
        difference_report.close()
comparefiles()

file=open('C:\\Users\\User\\Downloads\\car_output.txt')
print(file)

#browser.find_element_by_name('vrm').send_keys('B67123')
#inputbox=browser.find_element_by_class_name('vrm')
#inputbox.send_keys('B67123')
#for registation in registrationnumbers(carRegex.findall(text)):
 #   print(registation)


