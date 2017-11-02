x_list = []
y_list = []

for i in range(8):
    x_y = input("Enter x and y : ").split()
    x_list.append(x_y[0])
    y_list.append(x_y[1])

answer = "NO"

for x in range(len(x_list)):
    for y in range(len(y_list)):
        if x != y:
            if int(x_list[x]) == int(x_list[y]) or int(y_list[x]) == int(y_list[y]) or abs(int(x_list[x])-int(x_list[y])) == abs(int(y_list[x])-int(y_list[y])):
                answer = "YES"

print(answer)