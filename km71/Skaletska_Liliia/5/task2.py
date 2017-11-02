
a = [int(i) for i in input().split()]

def elements(a, count, i):

    if i >= len(a):
        return count

    count = elements_inner(a, count, a[i], i + 1)

    return elements(a, count, i + 1)

def elements_inner(a, count, element, j):

    if j >= len(a):
        return count

    if a[j] == element:
        count += 1

    return elements_inner(a, count, element, j + 1)    

print(elements(a, 0, 0))
