# LeetCode 2796 - Repeat String
# https://leetcode.com/problems/repeat-string/


class Solution:
    def replicate(self, s: str, times: int) -> str:
        res = ""
        for _ in range(times):
            res += s
        return res
