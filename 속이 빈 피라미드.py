num=5
i=1

while i<num:
       j=0
       while j<2*(num-i):
              print('o', end='')
              j=j+1
       k=1
       while k<2*i:
              if  k ==1 or k==2*i-1:
                     print('*', end=' ')
              else:
                     print('o', end=' ')
              k=k+1
       print()
       i=i+1

while i==num:
       k=1
       while k<2*i:
              print('*', end=' ')
              k=k+1
       print()
       break
       


       
