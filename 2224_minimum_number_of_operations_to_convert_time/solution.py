# LeetCode 2224 - Minimum Number of Operations to Convert Time
# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def to_min(t: str) -> int:
            return (ord(t[0]) - 48) * 600 + (ord(t[1]) - 48) * 60 + (ord(t[3]) - 48) * 10 + (ord(t[4]) - 48)

        diff = to_min(correct) - to_min(current)
        ans = 0
        for step in (60, 15, 5, 1):
            ans += diff // step
            diff %= step
        return ans
