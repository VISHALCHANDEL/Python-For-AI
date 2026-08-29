nums = [4, 2, 7, 4, 2, 9, 7, 4, 3, 2, 9, 7, 7]

freq = {}
for i in nums:

    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

n = -1
maxfreq = -1
for key, value in freq.items():
    if value > maxfreq:
        maxfreq = value
        n = key


print(f'Number with max freq is {n} and its frequency is {maxfreq}')

    

