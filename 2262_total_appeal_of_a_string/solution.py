# LeetCode 2262 - Total Appeal of A String
# https://leetcode.com/problems/total-appeal-of-a-string/


class Solution:
    def appealSum(self, s: str) -> int:
        last = [-1] * 26
        ans = cur = 0
        for i, ch in enumerate(s):
            c = ord(ch) - 97
            cur += i - last[c]
            last[c] = i
            ans += cur
        return ans
