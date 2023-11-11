def isPalindrome(s: str):
    lower_case_alphanumeric: str = ''
    
    for char in s:
        if (isAlphanumeric(char)):
            lower_case_alphanumeric += char.lower()
    
    pointer_one = 0
    pointer_two = len(lower_case_alphanumeric) - 1
    
    while (pointer_one < pointer_two):
    
        if (lower_case_alphanumeric[pointer_one] != lower_case_alphanumeric[pointer_two]):
            return False
        
        pointer_one += 1
        pointer_two -= 1
        
    return True


def isAlphanumeric(s: str) -> bool:
    return s.isalnum()
