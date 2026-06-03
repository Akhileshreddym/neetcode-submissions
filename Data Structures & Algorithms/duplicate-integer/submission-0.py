class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            x = nums[i]
            if(x in seen):
                return True
            seen.add(x)
        return False