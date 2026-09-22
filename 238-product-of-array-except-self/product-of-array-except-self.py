class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # this one we need one for the prefix
        #one for the suffix and then multiply them all together to get the number

        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1,len(nums)):
            left[i] = nums[i-1] * left[i-1]
        
        for i in range(len(nums) - 2,-1,-1):
            right[i] = nums[i+1] * right[i+1]
        
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = left[i] * right[i]

        return res
