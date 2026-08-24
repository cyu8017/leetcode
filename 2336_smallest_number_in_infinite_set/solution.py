# LeetCode 2336 - Smallest Number in Infinite Set
# https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet:
    def __init__(self):
        self.next = 1
        self.added = set()
        self.heap = []

    def _bubbleUp(self, i: int) -> None:
        while i > 0:
            p = (i - 1) >> 1
            if self.heap[p] <= self.heap[i]:
                break
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def _bubbleDown(self, i: int) -> None:
        n = len(self.heap)
        while True:
            smallest = i
            l, r = i * 2 + 1, i * 2 + 2
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest == i:
                break
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            i = smallest

    def _push(self, x: int) -> None:
        self.heap.append(x)
        self._bubbleUp(len(self.heap) - 1)

    def _pop(self) -> int:
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._bubbleDown(0)
        return top

    def popSmallest(self) -> int:
        if self.heap:
            x = self._pop()
            self.added.discard(x)
            return x
        val = self.next
        self.next += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.next and num not in self.added:
            self.added.add(num)
            self._push(num)
