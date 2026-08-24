# LeetCode 2522 - Partition String Into Substrings With Values At Most K
# https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/


class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans = 1
        cur = 0
        for ch in s:
            d = ord(ch) - 48
            if d > k:
                return -1
            nxt = cur * 10 + d
            if nxt > k:
                ans += 1
                cur = d
            else:
                cur = nxt
        return ans
