from typing import List
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""


def longestConsecutive(nums: List[int]):

    longest = 0
    numSet = set(nums)

    for num in numSet:

        if num - 1 not in numSet:
            length = 1
            nextNumber = num + 1

            while nextNumber in numSet:
                length += 1
                nextNumber = nextNumber + 1

            longest = max(length, longest)

    return longest
