x1 = int(input("Enter a number from 1-8"))
y1 = int(input("Enter a number from 1-8"))
x2 = int(input("Enter a number from 1-8"))
y2 = int(input("Enter a number from 1-8"))
if ((x1 - x2) % 2 == (y1 - y2) % 2):
    print("YES")
else:
    print("NO")