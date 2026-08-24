# LeetCode 2889 - Reshape Data: Pivot
# https://leetcode.com/problems/reshape-data-pivot/

from typing import Any, List


class Solution:
    def pivotTable(self, weather: List[Any]) -> List[Any]:
        months = []
        by_month = {}
        for r in weather:
            if isinstance(r, list):
                city, month, temperature = r[0], r[1], r[2]
            else:
                city, month, temperature = r["city"], r["month"], r["temperature"]
            if month not in by_month:
                by_month[month] = {}
                months.append(month)
            by_month[month][city] = temperature
        return [{"month": month, **by_month[month]} for month in months]
