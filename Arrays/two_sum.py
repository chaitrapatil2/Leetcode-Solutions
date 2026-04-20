#Problem: Two Sum
#Approach: HashMap
#Time Complexity: O(n)

def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[nums[i]] = i