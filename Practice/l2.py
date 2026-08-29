l2 = [1, 3, 4, 5, 6, 7]

left = 0
right = len(l2) - 1

while(left <= right):
    temp = l2[left]
    l2[left] = l2[right]
    l2[right] = temp
    left = left + 1
    right = right - 1

for i in l2:
    print(i, end = " ")