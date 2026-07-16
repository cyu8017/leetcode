class Solution:
    def minOperations(self, s):
        alt1 = sum(s[i] != "01"[i & 1] for i in range(len(s)))
        return min(alt1, len(s) - alt1)
