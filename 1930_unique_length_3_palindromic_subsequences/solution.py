class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        ans = 0
        for c in first:
            if last[c] - first[c] > 1:
                ans += len(set(s[first[c] + 1:last[c]]))
        return ans
