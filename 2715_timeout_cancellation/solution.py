# LeetCode 2715 - Timeout Cancellation
# https://leetcode.com/problems/timeout-cancellation/

import threading
from typing import Any, Callable, List


class Solution:
    def cancellable(self, fn: Callable, args: List[Any], t: int) -> Callable[[], None]:
        timer = threading.Timer(t / 1000.0, lambda: fn(*args))
        timer.daemon = True
        timer.start()

        def cancel() -> None:
            timer.cancel()

        return cancel
