from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
            elif prices[right] > prices[left]:
                profite = prices[right] - prices[left]
                maxP = max(profite, maxP)
                right += 1
            else:
                right += 1

        return maxP


solver = Solution()
result = solver.maxProfit([3, 4, 5, 2, 6, 7])
print(result)