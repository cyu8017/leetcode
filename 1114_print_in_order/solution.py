# LeetCode 1114 - Print in Order
# https://leetcode.com/problems/print-in-order/

import threading


class Foo:
    def __init__(self) -> None:
        self._second = threading.Lock()
        self._second.acquire()
        self._third = threading.Lock()
        self._third.acquire()

    def first(self, output=None) -> None:
        write = output.write if output else (lambda s: print(s, end=""))
        write("first")
        self._second.release()

    def second(self, output=None) -> None:
        write = output.write if output else (lambda s: print(s, end=""))
        self._second.acquire()
        write("second")
        self._third.release()

    def third(self, output=None) -> None:
        write = output.write if output else (lambda s: print(s, end=""))
        self._third.acquire()
        write("third")
