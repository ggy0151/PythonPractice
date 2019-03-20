#피라미드 출력 1번
print('============================')

num=5
i=1
while i<= num:
    j=0
    while j<2*(num-i):
        print('_', end= '')
        j=j+1
    k = 1
    while k<2*i:
        print('*', end='_')
        k= k+1
    print()
    i = i+1

        
