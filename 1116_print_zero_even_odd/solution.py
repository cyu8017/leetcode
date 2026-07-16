# LeetCode 1116 - Print Zero Even Odd
# https://leetcode.com/problems/print-zero-even-odd/

import threading


class ZeroEvenOdd:
    def __init__(self, n: int) -> None:
        self.n = n
        self._zero = threading.Semaphore(1)
        self._even = threading.Semaphore(0)
        self._odd = threading.Semaphore(0)

    def zero(self, printNumber) -> None:
        for i in range(self.n):
            self._zero.acquire()
            printNumber(0)
            if i % 2 == 0:
                self._odd.release()
            else:
                self._even.release()

    def even(self, printNumber) -> None:
        for num in range(2, self.n + 1, 2):
            self._even.acquire()
            printNumber(num)
            self._zero.release()

    def odd(self, printNumber) -> None:
        for num in range(1, self.n + 1, 2):
            self._odd.acquire()
            printNumber(num)
            self._zero.release()
