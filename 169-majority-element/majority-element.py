class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        # how do i get the highest number count key in the dictionary?
        # max(count) = give me the biggest key
        # key=count.get means score each key using count.get(), then give me the key with the highest score
        # max(count,key=count.get) - score every key using count.get(), then give me the key with the highest score

        return max(count,key=count.get)