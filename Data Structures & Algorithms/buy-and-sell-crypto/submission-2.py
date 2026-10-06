class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r+=1
            else:
                curMax = prices[r] - prices[l]
                if curMax > max:
                    max = curMax
                r+=1
        return max 
