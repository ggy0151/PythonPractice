import random


def choose():
      number= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      random.shuffle(number)
      return str(number[0])+str(number[1])+str(number[2])
      


def drawBoard():
       print('=====================\n')
       print('Guess numbers (000~999):')
       print('_'*3)

def inputNumber():
       answer=input()
       if(answer[0]==answer[1]==answer[2]):
              print('각기 다른 숫자 3개 입력하기')
              
       elif(answer[0]==answer[1]):
              print('각기 다른 숫자 3개 입력하기')
              
       elif(answer[0]==answer[2]):
              print('각기 다른 숫자 3개 입력하기')
              
       elif(answer[1]==answer[2]):
              print('각기 다른 숫자 3개 입력하기')
              
       else:
              pass
       return answer 
       
                     
def Result(num, le):
       strike=0
       ball=0
       for i in range(0,3):
              for j in range(0, 3):
                     
                     if num[i]== le[j] and i==j:  
                             strike+=1
                             
                     elif num[i]==le[j] and i !=j:
                             ball+=1
                             
                            
       print(str(ball), 'Ball', str(strike), 'Strike')
       
              

def Win(num, le):
       return  (num[0]== le[0] and num[1]==le[1] and num[2]==le[2])

print('START\n')

strike = 0

while True:
       theNumber=choose()
       gameisPlaying = True

       while gameisPlaying:
              while strike<4:
                     drawBoard()
                     playeranswer=inputNumber()

                     Result(theNumber, playeranswer)
                     if Win(theNumber, playeranswer):
                            print('Yes! The secret number is " '+str(theNumber)+'"! You have won! ')
                            gameisPlaying = False
       
                     
       print('Do you want to play again?(yes or no)')
       if not input().lower().startswith('y'):
              break
       




