class Solution:
    def longestNiceSubstring(self, s):
        def nice(t):
            chars = set(t)
            return all(ch.swapcase() in chars for ch in chars)
        best = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if nice(s[i:j]) and j - i > len(best):
                    best = s[i:j]
        return best
