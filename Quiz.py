import random
#Create the quiz
capitals ={'Albama':'Montogomery','Arizona':'Phoenix','Colorado':'Denver','Georgia':'Atlanta','Hawaii':'Honolulu',
           'Oklahoma':'Oklahoma City','Texas':'Austin','New Yonk':'Albany','Massachusetts':'Boston','Ohio':'Columbus'}



for quizNum in range(10):
    quizFile=open('capitalsquiz%s.txt' % (quizNum+1),'w')
    answerkeyFile=open('capitalsquiz_answers%s.txt' % (quizNum+1),'w')

# Write the header of the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '* 20) + 'State Capitals Quiz (Form %s)' %(quizNum +1))
    quizFile.write('\n\n')

#Shuffle the order of the states
    states=list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(10):
        quizFile.write('%s.What is the capital of %s?\n' % (questionNum+1,states[questionNum]))

'''
for questionNum in range(10):
    correctAnswer = capitals[states[questionNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers=random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

'''