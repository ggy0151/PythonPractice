#덧셈 함수
def add(a,b):
       return a+b


#뺄셈 함수
def sub(a,b):
       return a-b



#곱셈 함수
def mul(a,b):
       return a*b



#나눗셈 함수
def div(a,b):
       return a/b


def main():
    print('first operand is 0')
    result=float(0)
    while True:
           print('operator(+, -, *, /, exit)\n >>>')
           operator=input()
           if operator in '+-*/':
                  print('operand\n >>>')
                  operand=float(input())
                  if operator=='+':
                         result=add(result, operand)
                         print('result')
                         print('----------------------')
                         print(result)
                         print('----------------------')
                  elif operator=='-':
                         result=sub(result, operand)
                         print('result')
                         print('----------------------')
                         print(result)
                         print('----------------------')
                  elif operator=='*':
                         result=mul(result, operand)
                         print('result')
                         print('----------------------')
                         print(result)
                         print('----------------------')
                  elif operator=='/':
                         result=div(result, operand)
                         print('result')
                         print('----------------------')
                         print(result)
                         print('----------------------')
           elif operator=='exit':
                  print('종료되었습니다.\n')
                  break
           else:
                  print('잘못 입력하셨습니다.\n')
                         


if __name__ == '__main__':
    main()
