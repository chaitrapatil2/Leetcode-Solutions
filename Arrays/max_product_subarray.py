# Maximum Product Subarray

def maxProduct(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max_prod * curr, min_prod * curr)
        min_prod = min(curr, max_prod * curr, min_prod * curr)
        max_prod = temp_max

        result = max(result, max_prod)

    return result