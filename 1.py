'''a = int(input("enter a "))
b = int(input("enter b "))
a = int(input())
b = int(input())
c = a**2
d = b**2

if c == b:
    print(" a is sqare of b")
elif a==d:
    print(" b is sqare of a")
else:
    print(" _____ ")
    
    
    if a == b**2 or b == a**2:
    print("yes")
else:
    print('no')
 

from random import randint

n = 5
nums = [randint(95, -15) for i in range(n)]
print(nums)

n_max = nums[0]

for i in range(n):
    if nums[i] > n_max : n_max = nums[i]

print(n_max)
  

n = int(input("enter the N-number "))

for i in range(-n, n + 1):
    print(i, end=" ")




a = float(input())

a = a * 10 % 10

print(int(a))
''

a = int(input("enter the number "))


if ((a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and (a % 30 != 0)):
    print('true')
else:
    print('false')

print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x == z or x <= y and z):
                print(x, y, z)
                
import math

print(math.sqrt(811))
print(f"{811**0.5:.4f}")'''