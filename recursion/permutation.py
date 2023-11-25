def permute(s: str):
    
    out = []
    
    if len(s) == 1:
        out = [s]
    
    else:
        for idx, letter in enumerate(s):
            
            for perm in permute(s[:idx] + s[idx+1:]):
                out += [letter + perm]
    
    return out

ans = permute('abc')
print(ans)