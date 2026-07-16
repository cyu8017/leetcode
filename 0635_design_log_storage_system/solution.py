# LeetCode 0635 - Design Log Storage System
# https://leetcode.com/problems/design-log-storage-system/

from typing import List


class LogSystem:
    def __init__(self):
        self.logs: list[tuple[int, str]] = []
        self.granularity_index = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19,
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        index = self.granularity_index[granularity]
        start_key = start[:index]
        end_key = end[:index]
        matched = [
            (timestamp, log_id)
            for log_id, timestamp in self.logs
            if start_key <= timestamp[:index] <= end_key
        ]
        matched.sort()
        return [log_id for _, log_id in matched]
