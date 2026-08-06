class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for i in range(len(nums)):
            if(nums[i] in elements):
                elements[nums[i]] = elements[nums[i]] + 1
            else:
                elements[nums[i]] = 1
        sortedElements = dict(sorted(elements.items(), key = lambda x:x[1], reverse = True))
        mostFreq = list(sortedElements.keys())[:k]
        return mostFreq