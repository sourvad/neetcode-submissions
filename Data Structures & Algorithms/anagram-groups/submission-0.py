class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        res = []

        for s in strs:
            wordKey = [0] * 26

            for c in s:
                wordKey[ord(c) - ord('a')] += 1

            wordKey = tuple(wordKey)

            if wordKey in anagrams:
                anagrams[wordKey].append(s)
            else:
                anagrams[wordKey] = [s]

        for key in anagrams:
            res.append(anagrams[key])
        
        return res