# Problem: Maximum Subarray

def maxSubArray(nums):
    current = max_sum = nums[0]
    for n in nums[1:]:
        current = max(n, current + n)
        max_sum = max(max_sum, current)
    return max_sum