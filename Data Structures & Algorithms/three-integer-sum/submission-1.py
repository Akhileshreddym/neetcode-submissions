class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = set()
        for i in range(len(nums)):
            number1 = nums[i]
            left = i+1
            right = len(nums) - 1
            goal = 0 - number1
            while(left < right):
                currentNum = nums[left] + nums[right]
                if (currentNum > goal):
                    right -= 1
                elif (currentNum < goal):
                    left += 1
                elif (currentNum == goal):
                    if (number1, nums[left], nums[right]) not in solutions:
                        solutions.add((number1,nums[left],nums[right]))
                    left += 1
                    right -= 1
                    
        return list(solutions)
        