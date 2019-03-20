n = int(input('근무 시간을 입력하시오 :'))
price = int(input('시간당 수당을 입력하시오 : '))

if n >= 12:
    addSalary = price*(n-12)*1.3
    totalSalary = price*12 + addSalary
else :
    totalSalary = price*n
print("총 급여는", totalSalary, '원입니다.')
