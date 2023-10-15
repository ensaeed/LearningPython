
for quizNum in range(35):
#Create the quiz and answer key files
    quizFile=open('capitalsquiz%s.txt' % (quizNum+1),'w')
    answerKeyFile= ('capitalsquiz_answers%s.txt' %(quizNum+1),'w')