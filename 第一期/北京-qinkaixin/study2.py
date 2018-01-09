import random

a = []
for i in range(0,100):
    x = random.randint(10,1000)
    a.append(x)
print(a)

# list.sort(a)
# print(a)

# a.sort()
# print(a)
for i in range(len(a)):
    for j in range(i):
        if a[j] > a[i]:
            a[j], a[i] = a[i], a[j]
print(a)






