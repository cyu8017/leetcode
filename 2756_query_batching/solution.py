# LeetCode 2756 - Query Batching
# https://leetcode.com/problems/query-batching/

import time
from typing import Callable, List


class QueryBatcher:
    def __init__(self, queryMultiple: Callable, t: int):
        self.queryMultiple = queryMultiple
        self.t = t
        self.pending = []
        self.busyUntil = 0.0
        self.timer = None

    async def getValue(self, key: str) -> str:
        import asyncio

        loop = asyncio.get_event_loop()
        fut = loop.create_future()
        now = time.time() * 1000
        self.pending.append({"key": key, "resolve": fut})
        if now >= self.busyUntil:
            self.flush()
        elif self.timer is None:
            delay = max(0.0, (self.busyUntil - now) / 1000.0)

            def fire():
                self.timer = None
                self.flush()

            self.timer = loop.call_later(delay, fire)
        return await fut

    def flush(self) -> None:
        if not self.pending:
            return
        batch = self.pending
        self.pending = []
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None
        self.busyUntil = time.time() * 1000 + self.t
        keys = [b["key"] for b in batch]
        result = self.queryMultiple(keys)

        def apply(values: List[str]) -> None:
            for i, item in enumerate(batch):
                fut = item["resolve"]
                if not fut.done():
                    fut.set_result(values[i])

        if hasattr(result, "__await__"):
            import asyncio

            async def wait_and_apply():
                values = await result
                apply(values)

            asyncio.get_event_loop().create_task(wait_and_apply())
        else:
            apply(result)
