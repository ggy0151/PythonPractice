#구구단 반복문(while) input 정수 입력 구구단 출력

print('Input dan')
number=input()
print('***********'+number+'dan***********')
    
su1=int(number)
su2=1
while su2<=9:
    print(str(su1)+'*'+str(su2)+'='+str(su1*su2))
    su2+=1    
print('************************************')    
    
   
