# LeetCode 1188 - Design Bounded Blocking Queue
# https://leetcode.com/problems/design-bounded-blocking-queue/

import threading
from collections import deque


class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue: deque[int] = deque()
        self.not_full = threading.Semaphore(capacity)
        self.not_empty = threading.Semaphore(0)
        self.lock = threading.Lock()

    def enqueue(self, element: int) -> None:
        self.not_full.acquire()
        with self.lock:
            self.queue.append(element)
        self.not_empty.release()

    def dequeue(self) -> int:
        self.not_empty.acquire()
        with self.lock:
            value = self.queue.popleft()
        self.not_full.release()
        return value

    def size(self) -> int:
        with self.lock:
            return len(self.queue)
