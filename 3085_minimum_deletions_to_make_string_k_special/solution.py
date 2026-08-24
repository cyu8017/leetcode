# LeetCode 3085 - Minimum Deletions to Make String K-Special
# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - 97] += 1
        nums = [v for v in freq if v > 0]
        ans = len(word)
        for i in range(len(word) + 1):
            cur = 0
            for x in nums:
                if x < i:
                    cur += x
                elif x > i + k:
                    cur += x - i - k
            ans = min(ans, cur)
        return ans
