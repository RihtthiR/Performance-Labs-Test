
import sys

numbers_file = sys.argv[1] #numbers.txt

with open(numbers_file, 'r') as file:
    nums = [int(line.strip()) for line in file]

nums.sort()
if len(nums) % 2 == 0:
    median1, median2 = nums[len(nums) // 2], nums[(len(nums) - 1) // 2]
    print(min(sum(abs(num - median1) for num in nums), sum(abs(num - median2) for num in nums)))
else:
    median = nums[len(nums) // 2]
    print(sum(abs(num - median) for num in nums))