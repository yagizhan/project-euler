#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of
# the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

a = 0
d = 0
z = 0
y = 0
for i in range(1 ,101):
    x = i**2
    y += x
for k in range(1,101):
    z += k
    a = z ** 2
d = a - y
print(d)
