def inputNumber():
    print('Please input the last number')
    num=input()
    return num


def outputNumber(num):
    print('-----------start-------------')
    for count in range(1, int(num)+1):
           clap=0
           for answer in str(count):
                  if answer in '369' :
                         clap+=1
           if clap == 0:
                  print (count)
           else:
                  print('clap'*clap)
                  

while True:
       gameIsplaying = True
       while gameIsplaying:
              theNumber= inputNumber()
              outputNumber(theNumber)
              print('-----------end--------')
              gameIsplaying = False
              
       print('Do you want to play again?(yes or no)')
       if not input().lower().startwith('y'):
              break
