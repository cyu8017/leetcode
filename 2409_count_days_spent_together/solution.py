# LeetCode 2409 - Count Days Spent Together
# https://leetcode.com/problems/count-days-spent-together/

class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_day(s: str) -> int:
            m = (ord(s[0]) - 48) * 10 + (ord(s[1]) - 48)
            d = (ord(s[3]) - 48) * 10 + (ord(s[4]) - 48)
            res = d
            for i in range(m - 1):
                res += days[i]
            return res

        a1, a2 = to_day(arriveAlice), to_day(leaveAlice)
        b1, b2 = to_day(arriveBob), to_day(leaveBob)
        start = max(a1, b1)
        end = min(a2, b2)
        if end < start:
            return 0
        return end - start + 1
