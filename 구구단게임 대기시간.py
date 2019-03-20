import random
import time

question=0
print('*******START********\n')
while question<5 :
    num1=random.randint(1,9)
    num2=random.randint(1,9)
    print( str(num1)+' *' +str(num2)+ ' = ?')
    question=question+1
    time.sleep(3)
    result=input()
    if int(result) == int(num1)*int(num2):
        print('Correct Answer\n')
    if int(result) != int(num1)*int(num2):
        print('Wrong Answer,'+ str(num1)+' * '+str(num2)+' ='+ str(num1*num2)+' \n')
print('-------------------------')
