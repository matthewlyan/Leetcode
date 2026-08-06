class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        for this solution we are gonna do the sorted version

        so 1. create a hash map where each key is the sorted version fo the string and the value of it will be the list of strings belonging to that anagram group
        2. iterate through each string in the list
            sort the character of the string to form a key
            append the original string to the list corresponding to this key
        3. after processing all strings, return the values of the map
        """

        res = defaultdict(list)
        for s in strs:
            #sorted returns a list, so [a,e,t]
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())