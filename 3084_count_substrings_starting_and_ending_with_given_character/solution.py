# LeetCode 3084 - Count Substrings Starting and Ending with Given Character
# https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = 0
        for ch in s:
            if ch == c:
                cnt += 1
        return cnt * (cnt + 1) // 2
