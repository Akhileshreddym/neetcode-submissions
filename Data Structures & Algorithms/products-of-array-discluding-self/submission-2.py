class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        zeroCount = 0;
        for i in range(len(nums)):
            if(nums[i] != 0):
                product = product * nums[i]
            else:
                zeroCount += 1
        for i in range(len(nums)):
            if (zeroCount == 0):
                output.append(int(product/(nums[i])))
            elif (zeroCount == 1 and nums[i] == 0):
                output.append(int(product))
            else:
                output.append(0)
        return output