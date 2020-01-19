
n = int(input("Enter any number : "))
s = 2
while s<n:
    if n%s == 0:
        print(f"{n} Number is not prime...")
        break
    s += 1
else:
    print(f"{n} is prime")
