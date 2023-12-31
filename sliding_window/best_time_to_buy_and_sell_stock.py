from typing import List

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
def maxProfit(prices: List[int]):
    
    lowest = prices[0]
    max_profit = 0
    
    for price in prices:
        
        if price < lowest:
            lowest = price
            
        max_profit = max(max_profit, price - lowest)
        
    return max_profit


