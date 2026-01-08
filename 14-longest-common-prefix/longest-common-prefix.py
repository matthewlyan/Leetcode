class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # we use the strs[0] first word and try to concacnate a string until it doesnt match anymore
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            
            res += strs[0][i]
        
        return res