class Solution:
    def isDecomposable(self, s: str) -> bool:
        n = len(s)
        i = 0
        twos = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            length = j - i
            if length % 3 == 1:
                return False
            if length % 3 == 2:
                twos += 1
                if twos > 1:
                    return False
            i = j
        return twos == 1
