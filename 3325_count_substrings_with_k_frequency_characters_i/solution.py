# LeetCode 3325 - Count Substrings With K-Frequency Characters I
# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - 97] += 1
                if any(f >= k for f in freq):
                    ans += n - j
                    break
        return ans
