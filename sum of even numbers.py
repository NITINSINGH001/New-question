n= int(input("ENTER THE FIRST NUMBER"))
i = 1
s = 0
while i<= n:
    if i % 2 == 0:
        s = s + i
    i = i + 1

print('Even number sum', s)
