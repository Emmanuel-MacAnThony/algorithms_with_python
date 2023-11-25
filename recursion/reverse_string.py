def reverse_string(s: str):
    
    if len(s) == 1:
        return s[0]
    
    else:
        return s[len(s) - 1] + reverse_string(s[:len(s) - 1])
    
