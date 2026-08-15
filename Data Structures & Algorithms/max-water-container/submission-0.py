class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxAmount = 0
        while (left<right):
            width = right - left
            highestHeight = min(heights[left], heights[right])
            currentAmount = width * highestHeight
            if(currentAmount > maxAmount):
                maxAmount = currentAmount
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        return maxAmount
        