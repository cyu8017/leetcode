# LeetCode 1195 - Fizz Buzz Multithreaded
# https://leetcode.com/problems/fizz-buzz-multithreaded/

import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.condition = threading.Condition()

    def fizz(self, printFizz) -> None:
        self._run(lambda x: x % 3 == 0 and x % 5 != 0, lambda: printFizz())

    def buzz(self, printBuzz) -> None:
        self._run(lambda x: x % 5 == 0 and x % 3 != 0, lambda: printBuzz())

    def fizzbuzz(self, printFizzBuzz) -> None:
        self._run(lambda x: x % 15 == 0, lambda: printFizzBuzz())

    def number(self, printNumber) -> None:
        self._run(lambda x: x % 3 != 0 and x % 5 != 0, lambda: printNumber(self.current))

    def _run(self, predicate, action) -> None:
        with self.condition:
            while self.current <= self.n:
                if predicate(self.current):
                    action()
                    self.current += 1
                    self.condition.notify_all()
                else:
                    self.condition.wait()
