class Solution(object):
  def twoSum(object, nums, target):
    if len(nums) == 0:
      return []
    i = 0
    while (i < len(nums)):
      first = nums[i]
      if first < target:
        if len(nums[i:]) == 0:
          return []
        j = i + 1
        while (j < len(nums)):
          second = nums[j]
          if j < target:
            if (first + second) == target:
              return [i, j]

print(twoSum([2,7,11,15], 9))
