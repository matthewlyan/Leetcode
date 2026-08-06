class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        we need to use two pointers to swap so like if we run into the val when iterating through the nums array, we swap with whatever the r pointer is at, and then once we swap we decrement the right pointer by 1 and keep incrementing the l pointer

        i guess once the array is done iterating we can go through it and remove all of the vals
        """

        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return l
