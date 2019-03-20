number = int(input('정수를 입력하시오'))
count = 0
m = 1
while m <= number:
    if number % m == 0 :
        count += 1
        print(m)
    m += 1
print(number, '의 약수의 개수:', count) 
        
