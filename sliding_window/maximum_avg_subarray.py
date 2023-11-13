from typing import List

"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.
"""
def maximum_avg_subarray(nums: List[int], k: int) -> float:
    
    windowSum: int = 0
    start: int = 0
    max_avg = float('-inf')
    
    for end in range(len(nums)):
        windowSum += nums[end]
        if (end - start + 1 == k):
            max_avg = max(max_avg, windowSum/k)
            windowSum -= nums[start]
            start += 1
            print(max_avg)
        
    
    return max_avg

nums = [1,12,-5,-6,50,3]
k = 4

maximum_avg_subarray(nums, k)

            
