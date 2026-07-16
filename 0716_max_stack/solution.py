# LeetCode 0716 - Max Stack
# https://leetcode.com/problems/max-stack/


class MaxStack:
    def __init__(self):
        self.stack: list[int] = []
        self.maxes: list[int] = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.maxes.append(x if not self.maxes else max(x, self.maxes[-1]))

    def pop(self) -> int:
        self.maxes.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxes[-1]

    def popMax(self) -> int:
        max_val = self.peekMax()
        buffer: list[int] = []
        while self.top() != max_val:
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return max_val
