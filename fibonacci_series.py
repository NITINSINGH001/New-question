# fibonacci series

n = int(input('Enter the value of n:'))

a = 0
b = 1
print(a, b, end=' ')

while n-2:
     c = a + b
     print(c, end=' ')
     a, b = b, c
