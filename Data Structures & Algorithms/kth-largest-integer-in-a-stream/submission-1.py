class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.heap = []
        self.k = k

        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
            else:
                heapq.heappushpop(self.heap, num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]