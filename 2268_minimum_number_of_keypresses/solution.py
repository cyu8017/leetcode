# LeetCode 2268 - Minimum Number of Keypresses
# https://leetcode.com/problems/minimum-number-of-keypresses/


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1
        freq.sort(reverse=True)
        ans = 0
        for i in range(26):
            if freq[i] == 0:
                break
            ans += freq[i] * (i // 9 + 1)
        return ans
