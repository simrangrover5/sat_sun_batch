l = []
try:
    for i in range(5):
        l.append(int(input("Enter any value : " )))

    print(l)
except KeyboardInterrupt as e:
    print(e)

print(l)
