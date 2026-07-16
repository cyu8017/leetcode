# LeetCode 1117 - Building H2O
# https://leetcode.com/problems/building-h2o/

import threading


class H2O:
    def __init__(self) -> None:
        self._hydrogen = threading.Semaphore(2)
        self._oxygen = threading.Semaphore(0)
        self._lock = threading.Lock()
        self._count = 0

    def hydrogen(self, releaseHydrogen) -> None:
        self._hydrogen.acquire()
        with self._lock:
            self._count += 1
            if self._count == 2:
                self._oxygen.release()
        releaseHydrogen()

    def oxygen(self, releaseOxygen) -> None:
        self._oxygen.acquire()
        releaseOxygen()
        with self._lock:
            self._count = 0
            self._hydrogen.release()
            self._hydrogen.release()
