class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nonDupNums = set(nums)
        longest = 0
        for i in nums:
            if (i-1 not in nonDupNums):
                length = 1
                currentNum = i
                while(currentNum+1 in nonDupNums):
                    length += 1
                    currentNum += 1
                longest = max(length,longest)
        return longest