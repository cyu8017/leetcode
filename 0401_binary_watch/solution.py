# LeetCode 0401 - Binary Watch
# https://leetcode.com/problems/binary-watch/

from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result: list[str] = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count("1") + bin(minute).count("1") == turnedOn:
                    result.append(f"{hour}:{minute:02d}")
        return result
