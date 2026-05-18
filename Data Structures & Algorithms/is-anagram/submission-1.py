class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s:
            return not t
        
        if len(s) != len(t):
            return False

        counts = dict()

        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            counts[t[i]] = counts.get(t[i], 0) - 1

        for key in counts:
            if counts[key] != 0:
                return False
        
        return True