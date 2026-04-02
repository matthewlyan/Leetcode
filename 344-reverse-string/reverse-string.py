class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        # jsut swap the l and the r

        while l < r:
            tempL = s[l]
            s[l] = s[r]
            s[r] = tempL
            l += 1
            r -= 1
        

        # 
        