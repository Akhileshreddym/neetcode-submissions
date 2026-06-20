class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = []
        for i in range(len(nums)):
            singleOutput = 1
            for j in range(len(nums)):
                if (i != j):
                    singleOutput *= nums[j]
            output.append(singleOutput)
        return output