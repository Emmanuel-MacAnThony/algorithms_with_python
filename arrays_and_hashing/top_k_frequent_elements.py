"""
    Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order.
"""


def topKFrequent(nums, k):

    if (len(nums) == 1):
        return nums

    frequencyMap = {}

    for entry in nums:
        frequencyMap[entry] = 1 + frequencyMap.get(entry, 0)

    sortedFrequencies = sorted(
        frequencyMap.items(), reverse=True, key=lambda x: x[1])[:k]

    result = [k for k, v in sortedFrequencies]

    return result
