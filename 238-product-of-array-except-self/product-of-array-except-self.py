class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer[i] = product of everything to the left of i * product of everything to the right of i
        #prefix[i] - means multiply everything before index i, prefix[i-1] * nums[i-1]
        #suffix[i] - means multiply everything to the right of index i, suffix[i+1] * nums[i+1]

        #prefix[i-1] - everything before the previous guy
        #nums[i-1] - the previous guy

        # suffix[i+1] - everything after the next i
        # nums[i+1] - the next i

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        # suffix[2] = suffix[3] * nums[3] = 1 * 4 = 4
        # suffix = [1,1,4,1]

        #suffix[1] = suffix[2] * nums[2] = 4 * 3
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        
        return res







