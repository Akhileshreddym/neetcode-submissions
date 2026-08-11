class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        sortedList = []
        for i in range(len(nums)):
            if (sortedList and nums[i] == sortedList[-1]):
                continue
            sortedList.append(nums[i])
        highest = 1
        currentSeq = 1
        currentNum = sortedList[0]
        for i in range(1, len(sortedList)):
            if (sortedList[i] == currentNum+1):
                currentSeq += 1
            else:
                currentSeq = 1
            if (currentSeq > highest):
                highest = currentSeq
            currentNum = sortedList[i]
        return highest
        