# LeetCode 2725 - Interval Cancellation
# https://leetcode.com/problems/interval-cancellation/

import threading
from typing import Any, Callable, List


class Solution:
    def cancellable(self, fn: Callable, args: List[Any], t: int) -> Callable[[], None]:
        cancelled = False

        fn(*args)

        def loop() -> None:
            while not cancelled:
                if cancelled:
                    break
                timer = threading.Event()
                timer.wait(t / 1000.0)
                if not cancelled:
                    fn(*args)

        thread = threading.Thread(target=loop, daemon=True)
        thread.start()

        def cancel() -> None:
            nonlocal cancelled
            cancelled = True

        return cancel
