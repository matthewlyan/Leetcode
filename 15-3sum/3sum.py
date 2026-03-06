class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sort first so its easier to sort
        # [-4,-1,-1,0,1,2]
        nums.sort()
        res = []

        for i,a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                result = a + nums[l] + nums[r]
                if result < 0:
                    l += 1
                elif result > 0:
                    r -= 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    # make sure we dont get duplicates 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
                    
            
