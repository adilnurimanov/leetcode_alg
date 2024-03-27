class Solution(object):
  def twoSum(object, nums, target):
    if len(nums) == 0:
      return []
    hashmap = {}
    for i in range(len(nums)):
      hashmap[nums[i]] = i
    print(hashmap)
    for v in range(len(nums)):
      if v < target:
        dop = target - v
        if dop in hashmap:
          if (hashmap[v] != hashmap[dop]):
            return [hashmap[v], hashmap[dop]]

s = Solution()
print(s.twoSum([3,3,1], 6));
