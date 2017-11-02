a = [int(i) for i in input().split()]
x = int(input())
def place_in_the_ranks(a, x, index, i):

    if i >= len(a):
        return len(a) + 1

    if a[i] < x:
        index = i + 1
        return index

    return place_in_the_ranks(a, x, index, i + 1)

print(place_in_the_ranks(a, x, 1, 0))
