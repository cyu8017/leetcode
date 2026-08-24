# LeetCode 2805 - Custom Interval
# https://leetcode.com/problems/custom-interval/

import threading
from typing import Callable, Dict


class Solution:
    _next_id = 1
    _timers: Dict[int, threading.Timer] = {}
    _cancelled: Dict[int, Callable] = {}

    def customInterval(self, fn: Callable, delay: int, period: int) -> int:
        count = 0
        cancelled = False
        Solution._next_id += 1
        interval_id = Solution._next_id

        def schedule() -> None:
            nonlocal count

            def fire() -> None:
                nonlocal count
                if cancelled:
                    return
                fn()
                count += 1
                schedule()

            t = threading.Timer((delay + period * count) / 1000.0, fire)
            Solution._timers[interval_id] = t
            t.daemon = True
            t.start()

        def cancel() -> None:
            nonlocal cancelled
            cancelled = True
            t = Solution._timers.get(interval_id)
            if t:
                t.cancel()

        Solution._cancelled[interval_id] = cancel
        schedule()
        return interval_id

    def customClearInterval(self, interval_id: int) -> None:
        cancel = Solution._cancelled.get(interval_id)
        if cancel:
            cancel()
