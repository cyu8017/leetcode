# LeetCode 2776 - Convert Callback Based Function to Promise Based Function
# https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

import asyncio
from typing import Callable


class Solution:
    def promisify(self, fn: Callable) -> Callable:
        def wrapped(*args):
            loop = asyncio.get_event_loop()
            fut = loop.create_future()

            def callback(err, result=None):
                if fut.done():
                    return
                if err:
                    fut.set_exception(err if isinstance(err, BaseException) else Exception(err))
                else:
                    fut.set_result(result)

            fn(callback, *args)
            return fut

        return wrapped
