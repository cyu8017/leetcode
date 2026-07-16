# LeetCode 1172 - Dinner Plate Stacks
# https://leetcode.com/problems/dinner-plate-stacks/

import heapq


class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks: list[list[int]] = []
        self.available: list[int] = []

    def push(self, val: int) -> None:
        while self.available and (
            self.available[0] >= len(self.stacks) or len(self.stacks[self.available[0]]) == self.capacity
        ):
            heapq.heappop(self.available)
        if not self.available:
            self.stacks.append([])
            heapq.heappush(self.available, len(self.stacks) - 1)
        idx = self.available[0]
        self.stacks[idx].append(val)
        if len(self.stacks[idx]) == self.capacity:
            heapq.heappop(self.available)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return self.popAtStack(len(self.stacks) - 1) if self.stacks else -1

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        if len(self.stacks[index]) == self.capacity:
            heapq.heappush(self.available, index)
        return self.stacks[index].pop()
