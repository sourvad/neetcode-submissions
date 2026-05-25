class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = float('inf')

        for p in prices:
            if p < minPrice:
                minPrice = p
            else:
                profit = max(profit, p - minPrice)
        
        return profit