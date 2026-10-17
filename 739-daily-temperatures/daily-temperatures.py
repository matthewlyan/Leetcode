class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # use a monotatic stack for this question
        res = [0] * len(temperatures)
        stack = [] # we want to store the indicies here

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index

            stack.append(i)
        
        return res


