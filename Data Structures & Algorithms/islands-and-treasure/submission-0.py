class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
        q = []
        INF = 2147483647

        def isValid(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] != INF:
                return False
            
            return True

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((0, r, c))

        while q:
            dist, r, c = heapq.heappop(q)

            for dr, dc in neighbors:
                nr = r + dr
                nc = c + dc

                if isValid(nr, nc):
                    heapq.heappush(q, (dist + 1, nr, nc))
                    grid[nr][nc] = dist + 1

        return