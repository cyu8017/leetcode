# LeetCode 0636 - Exclusive Time of Functions
# https://leetcode.com/problems/exclusive-time-of-functions/

from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack: list[int] = []
        prev_time = 0

        for log in logs:
            func_id_str, event, time_str = log.split(":")
            func_id = int(func_id_str)
            time = int(time_str)

            if event == "start":
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(func_id)
                prev_time = time
            else:
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return result
