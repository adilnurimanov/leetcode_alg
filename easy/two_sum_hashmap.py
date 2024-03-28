class Solution(object):
  def twoSum(object, nums, target):
    if len(nums) == 0:
      return []
    hashmap = {}
    for i in range(len(nums)):
      if nums[i] not in hashmap:
        hashmap[nums[i]] = i
      else:
        valueindex = hashmap.pop(nums[i])
        print(valueindex)
        mylist = []
        mylist.append(valueindex)
        mylist.append(i)
        hashmap[nums[i]] = mylist
        print(mylist)
    print(hashmap)
    for v in hashmap:
      if v < target:
        dop = target - v
        if dop in hashmap:
          print('we are here 1')
          if type(hashmap[dop]) != list:
            if (hashmap[v] != hashmap[dop]):
              return [hashmap[v], hashmap[dop]]
          else:
            print('we are here 2')
            if v == dop:
              mylist = hashmap[dop]
              print(mylist)
              return mylist

s = Solution()
print(s.twoSum([3,3,1], 6));
