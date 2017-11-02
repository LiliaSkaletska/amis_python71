a = [int(i) for i in input().split()]
def elements(a, count, i):

    if i >= len(a):
        return count
    if once(a, i, 0):
        print(a[i])
    return elements(a, count, i + 1)
def once(a, element, j):
    if j >= len(a):
        return True
    if a[j] == a[element] and j != element:
        return False
    return once(a, element, j + 1)

elements(a, 0, 0)