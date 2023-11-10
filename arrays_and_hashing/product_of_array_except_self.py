from typing import List

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""


def productExceptSelf(nums: List[int]) -> List[int]:

    n = len(nums)

    productArray = [0] * n
    prefixArray = [0] * n
    suffixArray = [0] * n

    suffixArray[n-1] = 1
    for i in range(n-2, -1, -1):
        suffixArray[i] = nums[i + 1] * suffixArray[i+1]

    prefixArray[0] = 1
    for i in range(1, n):
        prefixArray[i] = nums[i-1] * prefixArray[i-1]

    for i in range(n):
        productArray[i] = prefixArray[i] * suffixArray[i]

    return productArray
