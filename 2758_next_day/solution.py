# LeetCode 2758 - Next Day
# https://leetcode.com/problems/next-day/

from datetime import datetime, timedelta


class Solution:
    def nextDay(self, date_value) -> str:
        if isinstance(date_value, datetime):
            d = date_value
        else:
            d = datetime.fromisoformat(str(date_value)[:10])
        nxt = d + timedelta(days=1)
        return f"{nxt.year:04d}-{nxt.month:02d}-{nxt.day:02d}"
