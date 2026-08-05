class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        we need to create two dictionaries where the dictionaries get a count of the characters of each string, if they are the same then its true else falase
        """

        count_s = {}
        for l in s:
            count_s[l] = 1 + count_s.get(l,0)
        
        count_t = {}
        for n in t:
            count_t[n] = 1 + count_t.get(n,0)
        
        return count_s == count_t