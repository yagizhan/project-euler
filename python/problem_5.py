#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

y = 1
for i in range(20, 1000000000, 20):
    if(y == 0):
        break
    for x in range(11, 21):
        if(i % x != 0):
            break
        if(x == 20):
            print(i)
            y = 0