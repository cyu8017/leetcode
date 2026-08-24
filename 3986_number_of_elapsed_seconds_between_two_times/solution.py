# LeetCode 3986 - Number of Elapsed Seconds Between Two Times
# https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/


class Solution:
    def toSeconds(self, s: str) -> int:
        h = (ord(s[0]) - ord("0")) * 10 + (ord(s[1]) - ord("0"))
        m = (ord(s[3]) - ord("0")) * 10 + (ord(s[4]) - ord("0"))
        sec = (ord(s[6]) - ord("0")) * 10 + (ord(s[7]) - ord("0"))
        return h * 3600 + m * 60 + sec

    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        return self.toSeconds(endTime) - self.toSeconds(startTime)
