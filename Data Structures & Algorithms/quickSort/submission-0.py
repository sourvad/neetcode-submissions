# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def sort(self, arr, start, end):
        if end - start + 1 <= 1:
            return

        pivot = end
        write = start

        for i in range(start, pivot):
            if arr[i].key < arr[pivot].key:
                arr[i], arr[write] = arr[write], arr[i]
                write += 1

        arr[write], arr[pivot] = arr[pivot], arr[write]
        
        self.sort(arr, start, write - 1)
        self.sort(arr, write + 1, end)

    
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs or len(pairs) == 1:
            return pairs

        self.sort(pairs, 0, len(pairs) - 1)
        return pairs
