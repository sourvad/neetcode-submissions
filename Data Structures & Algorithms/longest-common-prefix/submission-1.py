class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        i = 0

        while True:
            if i >= len(strs[0]):
                return "".join(ans)
                        
            cur = strs[0][i]

            for s in strs:
                if i >= len(s) or s[i] != cur:
                    return "".join(ans)
            
            ans.append(cur)
            i += 1
