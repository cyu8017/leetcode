# LeetCode 3329 - Count Substrings With K-Frequency Characters II
# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/


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
