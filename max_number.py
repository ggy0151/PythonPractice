a = int(input('정수를 입력하시오 :'))
max = a

count = 1
while count <= 4 :
    a = int(input('정수를 입력하시오 :'))
    if a > max:
        max = a
    count += 1
print()
print('가장 큰 값: ', max)
