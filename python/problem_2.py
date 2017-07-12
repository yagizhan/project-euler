#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fib1 = 1
fib2 = 1
sum = 0
fib = 0

while (fib < 4000000):
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    if fib % 2 == 0:
        sum += fib
print(sum)



