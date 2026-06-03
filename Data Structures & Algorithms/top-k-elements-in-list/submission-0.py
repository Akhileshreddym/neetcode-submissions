class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] = freq[i] + 1
            else:
                freq[i] = 1
        sortedDict= sorted(freq, key=lambda x:freq[x], reverse=True)
        result = []
        for i in range(k):
            result.append(sortedDict[i])
        return result