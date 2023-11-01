#Fibonacci sequence-->0 1 1 2 3 5 8 13 21 34
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
------------------or------------------
n = int(input("Enter the number of Fibonacci: "))
a, b = 0, 1
count = 0
while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1

Factorial->n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
n = int(input("Enter the number of Factorial sequenece number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"the factorial of {n} is {fact}")

"""Using Break to exit a loop when i==51 while
printing the values from 1 to 100"""

for i in range(1,100):
    print(i,end=" ")
    if i==51:
        break
---------------or---------------
i = 1
while i <= 100:
    print(i, end=' ')
    if i == 51:
        break
    i += 1


