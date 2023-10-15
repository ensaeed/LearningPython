import re

def strip(stringwithwhitespaces):
   print(stringwithwhitespaces.count(' '))



   # whiteSpace=re.compile(r'\w+')
   # mo=whiteSpace.findall(stringwithwhitespaces)
   whitesppacesremoved=stringwithwhitespaces.strip()
   print(whitesppacesremoved.count(' '))
  #  if mo==' ':
   #     whiteSpace.sub('')
   #     print(stringwithwhitespaces)



strip('  Its windy today  ')