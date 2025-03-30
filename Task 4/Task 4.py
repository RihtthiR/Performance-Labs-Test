
numbers_file = r"C:\Users\Riht\Desktop\Job\Performance Labs\Task 4\numbers.txt"

with open(numbers_file, 'r') as file:
    nums = [int(line.strip()) for line in file]

nums.sort()
median = nums[len(nums) // 2]
print(sum(abs(num - median) for num in nums))