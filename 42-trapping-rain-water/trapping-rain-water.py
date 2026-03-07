class Solution:
    def trap(self, height: List[int]) -> int:
        # limiting factor is the shortest wall, because water can just go over it
        # so we want to find the shortest wall on both sides left and right using two pointers.

        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        water = 0

        while l < r:
            if height[l] < height[r]:
                if maxLeft < height[l]:
                    maxLeft = height[l]
                else:
                    water += maxLeft - height[l]
                l += 1
            else:
                if maxRight < height[r]:
                    maxRight = height[r]
                else:
                    water += maxRight - height[r]
                r -= 1
        
        return water