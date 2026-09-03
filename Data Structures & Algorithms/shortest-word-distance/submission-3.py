class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        words = set([word1, word2])
        first = -1
        res = float('inf')

        for i in range(len(wordsDict)):
            if wordsDict[i] in words:
                if first == -1: 
                    first = i
                else:
                    res = min(res, i - first)
                    first = i

        return res