freq = {}

nums = [4, 2, 7, 4, 2, 9, 7, 4, 3, 2, 9, 7, 7]

for i in nums:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1


for i , j in freq.items():
    print(f'key is {i}, and value is {j}')

