# LeetCode 1185 - Day of the Week
# https://leetcode.com/problems/day-of-the-week/

import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.date(year, month, day).strftime("%A")
