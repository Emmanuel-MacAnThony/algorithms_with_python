from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(nums: List[int], target: int) -> List[int]:

    pointer_one = 0
    pointer_two = len(nums) - 1
    indexMap = {}

    for idx, num in enumerate(nums, start=0):
        indexMap[num] = [idx] + indexMap.get(num, [])

    nums = sorted(nums)

    while pointer_one < pointer_two:
        sum = nums[pointer_one] + nums[pointer_two]

        if (sum == target):

            if (nums[pointer_one] == nums[pointer_two]):
                return [indexMap[nums[pointer_one]][0], indexMap[nums[pointer_one]][1]]
            else:
                return [indexMap[nums[pointer_one]][0], indexMap[nums[pointer_two]][0]]

        if (sum < target):
            pointer_one += 1

        if (sum > target):
            pointer_two -= 1
