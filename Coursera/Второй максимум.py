n = int(input())
q = 0
s = 0
while n != 0:
    if q < n:
        s = q
        q = n
    else:
        if s < n:
            s = n
    n = int(input())
print(s)
