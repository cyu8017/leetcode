# LeetCode 1118 - Number of Days in a Month
# https://leetcode.com/problems/number-of-days-in-a-month/

import calendar


class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        return calendar.monthrange(year, month)[1]
