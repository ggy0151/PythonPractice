a=[1,2,3,4,5,6,7,8,9,10]
print(a[:])
print(a[6])
print(a[-2])
print(a[0:-2:2])
b = [13,14,15,16]
K = b + a
print(K)
print(b*2)
b.append(10)
print(b)
a.extend(b)
K.index(13)
m = []
m.extend(b)
m.insert(2,8)
m.append(3)
print(m)
m.sort()
print(m)
m.reverse()
print(m)
m.pop(4)
print(m)
m.remove(8)
print(m)




