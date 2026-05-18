class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s:
            return not t
        
        if len(s) != len(t):
            return False

        sCounts = dict()
        tCounts = dict()

        for i in range(len(s)):
            sCounts[s[i]] = sCounts.get(s[i], 0) + 1
            tCounts[t[i]] = tCounts.get(t[i], 0) + 1

        if len(sCounts) != len(tCounts):
            return False
        
        for key in sCounts:
            if key not in tCounts or tCounts[key] != sCounts[key]:
                return False
        
        return True