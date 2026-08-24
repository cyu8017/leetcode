# LeetCode 2676 - Throttle
# https://leetcode.com/problems/throttle/

import threading
import time
from typing import Any, Callable


class Solution:
    def throttle(self, fn: Callable, t: int) -> Callable:
        last = float("-inf")
        pending = None
        timer = None
        lock = threading.Lock()

        def run(*args: Any) -> None:
            nonlocal last
            last = time.time() * 1000
            fn(*args)

        def wrapper(*args: Any) -> None:
            nonlocal pending, timer
            with lock:
                now = time.time() * 1000
                remaining = t - (now - last)
                if remaining <= 0:
                    if timer is not None:
                        timer.cancel()
                        timer = None
                    run(*args)
                else:
                    pending = args
                    if timer is None:
                        def later() -> None:
                            nonlocal timer, pending
                            with lock:
                                timer = None
                                if pending is not None:
                                    a = pending
                                    pending = None
                                    run(*a)

                        timer = threading.Timer(remaining / 1000.0, later)
                        timer.daemon = True
                        timer.start()

        return wrapper
