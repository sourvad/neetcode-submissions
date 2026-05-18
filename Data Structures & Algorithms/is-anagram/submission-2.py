class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s:
            return not t
        
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1

        for freq in counts:
            if freq != 0:
                return False
        
        return True