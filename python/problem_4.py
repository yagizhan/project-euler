#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


y = 0
for z in range(999, 100, -1):
    for v in range(z , 100, -1):
        x = z * v
        if x > y:
            s = str(z * v)
            if s == s[::-1]:
                y = z * v
print(y)