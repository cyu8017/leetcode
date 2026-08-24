# LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
# https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        cnt.sort()
        ans = 0
        for i in range(26 - k):
            ans += cnt[i]
        return ans
