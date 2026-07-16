# LeetCode 1154 - Day of the Year
# https://leetcode.com/problems/day-of-the-year/

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))
        leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        days = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days[: month - 1]) + day
