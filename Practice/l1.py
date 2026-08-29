nums = [4, 7, 2, 7, 9, 2, 7]

if len(nums) < 2:
    print("2nd Largest doesnt exits")

largest  = nums[0]
secondLargest = int(-1e9)

for i in nums:
    if(i > largest):
        secondLargest = largest
        largest = i
    elif i < largest and i > secondLargest:
        secondLargest = i

print(f'Largest element {largest} and second largest is {secondLargest}')
