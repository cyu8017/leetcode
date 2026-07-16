# LeetCode 1115 - Print FooBar Alternately
# https://leetcode.com/problems/print-foobar-alternately/

import threading


class FooBar:
    def __init__(self, n: int) -> None:
        self.n = n
        self._foo = threading.Semaphore(1)
        self._bar = threading.Semaphore(0)

    def foo(self, output=None) -> None:
        write = output.write if output else (lambda s: print(s, end=""))
        for _ in range(self.n):
            self._foo.acquire()
            write("foo")
            self._bar.release()

    def bar(self, output=None) -> None:
        write = output.write if output else (lambda s: print(s, end=""))
        for _ in range(self.n):
            self._bar.acquire()
            write("bar")
            self._foo.release()
