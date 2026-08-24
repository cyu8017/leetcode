# LeetCode 3016 - Minimum Number of Pushes to Type Word II
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/


class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = [0] * 26
        for i in range(len(word)):
            cnt[ord(word[i]) - 97] += 1
        cnt.sort()
        ans = 0
        for i in range(26):
            ans += (i // 8 + 1) * cnt[26 - i - 1]
        return ans
