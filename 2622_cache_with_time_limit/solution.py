# LeetCode 2622 - Cache With Time Limit
# https://leetcode.com/problems/cache-with-time-limit/

import time
from typing import Any


class TimeLimitedCache:
    def __init__(self):
        self.data = {}

    def set(self, key: int, value: int, duration: int) -> bool:
        now = int(time.time() * 1000)
        e = self.data.get(key)
        alive = e is not None and e["expire"] > now
        self.data[key] = {"value": value, "expire": now + duration}
        return alive

    def get(self, key: int) -> int:
        now = int(time.time() * 1000)
        e = self.data.get(key)
        if e is None or e["expire"] <= now:
            return -1
        return e["value"]

    def count(self) -> int:
        now = int(time.time() * 1000)
        cnt = 0
        dead = []
        for k, e in self.data.items():
            if e["expire"] > now:
                cnt += 1
            else:
                dead.append(k)
        for k in dead:
            del self.data[k]
        return cnt


class Solution:
    def TimeLimitedCache(self, actions: Any = None) -> TimeLimitedCache:
        return TimeLimitedCache()
