import random
import datetime

# randint()----------> 

n = random.randint(2,8)
print(n)

n1 = random.randint(2,4)
print(n1)

# choice()--------> 

l = [10,34,23,67]
lc = random.choice(l)
print(lc)

list = ["Apple","Banana","Orang","Cherry"]
list_ch = random.choice(list)
print(list_ch)

# random()-----------> 

r = random.random()
print(r)

# shuffle()---------> 

random.shuffle(l)
print(l)

# uniform()-----------> 

u = random.uniform(3,9)
print(u)

# ~~~~~~~~~~~~~~~~~~DateTime~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = datetime.datetime.now()   
print(x)                   #output 2023-10-18 23:58:28.203663

y = datetime.datetime(2022,10,31)   
print(y)                   #output 2022-10-31 00:00:00

now = datetime.datetime.now()
m = now.strftime("%Y")
print(m)

now = datetime.datetime.now()
B = now.strftime("%B")
print(B)

now = datetime.datetime.now()
b = now.strftime("%b")
print(b)

I = now.strftime("%I")
print(I)