"""
Given a string s, find the length of the longest  substring without repeating characters.
"""
def lengthOfLongestSubstring(s):
    charset = set()
    maxl = 0
    l = 0
    
    for r in range(len(s)):
        
        while(s[r] in charset):
            charset.remove(s[l])
            l += 1
        
        charset.add(s[r])
        maxl = max(maxl, r - l + 1)
    
    return maxl