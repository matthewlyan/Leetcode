class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # array = [], and size is 2n
        res = []
        for i in range(2):
            for j in nums:
                res.append(j)
        
        return res