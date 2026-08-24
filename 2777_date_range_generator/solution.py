# LeetCode 2777 - Date Range Generator
# https://leetcode.com/problems/date-range-generator/

from datetime import datetime, timedelta
from typing import Generator, List, Union


class Solution:
    def dateRangeGenerator(
        self, start: str, end: str, step: int
    ) -> Union[List[str], Generator[str, None, None]]:
        def gen() -> Generator[str, None, None]:
            cur = datetime.fromisoformat(start)
            last = datetime.fromisoformat(end)
            while cur <= last:
                yield f"{cur.year:04d}-{cur.month:02d}-{cur.day:02d}"
                cur = cur + timedelta(days=step)

        return list(gen())
