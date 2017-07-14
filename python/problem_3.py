#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

number = 600851475143
y = 2
while y * y < number:
    while number % y == 0:
        number = number / y
    y = y + 1
print(int(number))
