import os
import re
cwd = os.getcwd()
file = open(cwd + "sections.txt","r")

pairs = file.readlines()
# PART 1  
# count = 0
# for pair in pairs:
#     nums = re.findall("\d+",pair)
#     nums = [int(num) for num in nums]
#     if (nums[0] >= nums[2] and nums[1] <= nums[3]) or (nums[0] <= nums[2] and nums[1] >= nums[3]):
#         count += 1

# print(count)

#PART 2
count = 0
for pair in pairs:
    nums = re.findall("\d+",pair)
    nums = [int(num) for num in nums]
    if (nums[0] >= nums[2] and nums[0] <= nums[3]) or (nums[2] >= nums[0] and nums[2] <= nums[1]):
        count += 1

print(count)