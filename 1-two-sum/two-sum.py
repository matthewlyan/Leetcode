class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {} # dictionary to store indicies
        for i,n in enumerate(nums):
            complement = target-n
            if complement in two_sum:
                return [two_sum[complement],i]
            two_sum[n] = i
        
        return []