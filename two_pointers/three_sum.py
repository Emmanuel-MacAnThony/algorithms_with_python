"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
def threeSum(nums):
    
    tripletMap = {}
    tripletArray = []
    nums = sorted(nums)
    
    for idx in range(1, len(nums)):
        
        pointer_one = 0
        pointer_two = len(nums) - 1
        
        while (pointer_one < idx and pointer_two > idx):
            i = nums[idx]
            j = nums[pointer_one]
            k = nums[pointer_two]
            sum = i + j + k
            key = "{i}{j}{k}".format(i=i, j=j, k=k)
            
            if (sum == 0):
                tripletMap[key] = tripletMap.get(key, [i, j,k])
                pointer_two -= 1
                continue
            
            if (sum > 0):
                pointer_two -= 1
                
            if (sum < 0):
                pointer_one += 1
                
    for key in tripletMap:
        tripletArray.append(tripletMap[key])
        
    
    return tripletArray
                
            
        
        
    