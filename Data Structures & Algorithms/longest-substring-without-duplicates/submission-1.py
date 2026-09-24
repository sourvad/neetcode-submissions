class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                res = max(res, r - l)
                l = seen[s[r]] + 1

            seen[s[r]] = r
            r += 1

        res = max(res, r - l)

        return res