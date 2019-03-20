import random
import time

question=0
print('*******START********\n')
while question<5 :
    num1=random.randint(1,9)
    num2=random.randint(1,9)
    num3=random.randint(1,9)
    num4=random.randint(1,9)
    print( str(num1)+'*' +str(num2)+'+'+str(num3)+'-'+str(num4)+ ' = ?')
    question=question+1
    print('1, ', end=' ' )
    time.sleep(1)
    print('2, ', end=' ' )
    time.sleep(1)
    print('3 : ', end=' ' )
    time.sleep(1)
    result=input()
    if int(result) == int(num1)*int(num2)+int(num3)-int(num4):
        print('Correct Answer\n')
    if int(result) != int(num1)*int(num2)+int(num3)-int(num4):
        print('Wrong Answer,'+ str(num1)+' * '+str(num2)+'+'+str(num3)+'-'+str(num4)+' ='+ str(num1*num2)+' \n')
print('-------------------------')

