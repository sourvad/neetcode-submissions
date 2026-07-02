class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(num):
            if len(cur) == k:
                res.append(cur.copy())
                return

            if num == n + 1:
                return

            dfs(num + 1)
            cur.append(num)
            dfs(num + 1)
            cur.pop()

        dfs(1)

        return res 