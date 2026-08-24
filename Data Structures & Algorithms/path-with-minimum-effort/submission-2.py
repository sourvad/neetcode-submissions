class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        import heapq

        ROWS = len(heights)
        COLS = len(heights[0])
        neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))

        seen = set()
        heap = [(0, 0, 0)]

        def validNeighbor(r, c):
            if r == ROWS or c == COLS or r == -1 or c == -1 or (r, c) in seen:
                return False
            
            return True
    
        while heap:
            cost, r, c = heapq.heappop(heap)

            if r == ROWS - 1 and c == COLS - 1:
                return cost
            
            if (r, c) in seen:
                continue
            
            seen.add((r, c))
            
            for dr, dc in neighbors:
                nr = r + dr
                nc = c + dc
                
                if validNeighbor(nr, nc):
                    newCost = max(cost, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(heap, (newCost, nr, nc))

        return -1
