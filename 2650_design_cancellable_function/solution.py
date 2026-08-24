# LeetCode 2650 - Design Cancellable Function
# https://leetcode.com/problems/design-cancellable-function/

import asyncio
from typing import Any, Callable, Generator, List, Tuple


class Solution:
    def cancellable(self, generator: Generator) -> List[Any]:
        cancelled = False

        def cancel() -> None:
            nonlocal cancelled
            cancelled = True

        async def run() -> Any:
            nonlocal cancelled
            nxt = next(generator)
            while True:
                try:
                    if asyncio.iscoroutine(nxt) or hasattr(nxt, "__await__"):
                        value = await nxt
                    else:
                        value = nxt
                    if cancelled:
                        nxt = generator.throw(Exception("Cancelled"))
                        continue
                    nxt = generator.send(value)
                except StopIteration as e:
                    return e.value
                except Exception as e:
                    try:
                        nxt = generator.throw(e)
                    except StopIteration as se:
                        return se.value

        return [cancel, run()]
