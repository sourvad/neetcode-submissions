class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0

        for i in range(len(t)):
            while j < len(s):
                if t[i] == s[j]:
                    break

                j += 1
            else:
                return len(t) - i

            j += 1
        
        return 0