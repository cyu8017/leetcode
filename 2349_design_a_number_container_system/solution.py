# LeetCode 2349 - Design a Number Container System
# https://leetcode.com/problems/design-a-number-container-system/

class NumberContainers:
    def __init__(self):
        self.idx = {}
        self.heap = {}

    def change(self, index: int, number: int) -> None:
        self.idx[index] = number
        if number not in self.heap:
            self.heap[number] = []
        self.heap[number].append(index)

    def find(self, number: int) -> int:
        h = self.heap.get(number)
        if not h:
            return -1
        h.sort()
        while h:
            i = h[0]
            if self.idx.get(i) == number:
                return i
            h.pop(0)
        return -1
