# LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        last = {ch: [-1] for ch in set(s)}
        for i, ch in enumerate(s):
            last[ch].append(i)
        for ch in last:
            last[ch].append(n)
        ans = 0
        for indices in last.values():
            for k in range(1, len(indices) - 1):
                ans += (indices[k] - indices[k - 1]) * (indices[k + 1] - indices[k])
        return ans
