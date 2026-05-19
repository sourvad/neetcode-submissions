class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        i = 0
        N = float('inf')

        for s in strs:
            N = min(N, len(s))

        for i in range(N):
            cur = strs[0][i]

            for s in strs:
                if cur != s[i]:
                    return "".join(ans)
        
            ans.append(cur)
        
        return "".join(ans)