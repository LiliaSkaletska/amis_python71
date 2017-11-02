N = int(input("Enter a number of pins: "))
K = int(input("Enter a number of ball throws: "))
l_list = []
r_list = []
pin_list = []


for i in range(K):
    l_r = input("Enter a number of pins that were knocked down using a '-' (l-r): ").split("-")
    l_list.append(l_r[0])
    r_list.append(l_r[1])

print(l_list)
print(r_list)

for s in range(N):
    pin_list.append('|')

for j in range(K):
    for pin in range(int(l_list[j]), int(r_list[j])+1):
        del pin_list[pin-1]
        pin_list.insert(pin-1, '.')


for e in range(len(pin_list)):
    print(pin_list[e], end = " ")
