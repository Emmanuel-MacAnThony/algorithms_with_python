"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations
"""
def characterReplacement(s: str, k: int):
    
    l = 0
    maxf = 0
    maxl = 0
    char_count = {}
    
    for r in range(len(s)):
        
        char_count[s[r]] = 1 + char_count.get(s[r], 0)
        maxf = max(char_count[s[r]], maxf)

        
        if (r - l + 1) - maxf > k:
            char_count[s[l]] -= 1
            l += 1
        
        maxl = max(maxl, r - l + 1)
    
    return maxl
        
        
        
        
        
        
        
        
    
    