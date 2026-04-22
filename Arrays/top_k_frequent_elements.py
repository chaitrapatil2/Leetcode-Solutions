# Top K Frequent Elements

from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]