
import math
start = int(input("Enter start number : "))
end = int(input("Enter end number : "))
l = []
while start<=end:
    print(start,end=',')
    s = 2
    while s<=math.sqrt(start):
        if start%s == 0:
            break
        s += 1
    else:
        if start == 2:
            pass
        else:
            l.append(start)
    start += 1
print()
print(*l)
