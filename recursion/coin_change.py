def coin_change(target, coins):
    
    min_coins = target
    
    if target in coins:
        return 1
    
    else:
        for coin in [c for c in coins if c <= target]:
            num_coins  = 1 + coin_change(target - coin, coins)
            
            if num_coins < min_coins:
                min_coins = num_coins
            
    
    return min_coins