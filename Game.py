import random

li = ["*"]

for i in range(1,20):
    li.append(i)
for i in range(11,20):
    li.append(i)
for i in range(21,30):
    li.append(i)

for i in range(0,20):
    n=input()
    c = random.choice(li)
    print(c)
    li.remove(c)